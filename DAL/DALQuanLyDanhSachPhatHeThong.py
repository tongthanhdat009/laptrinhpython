from DAL.dbconnector import Database
from DTO.DTODanhSachPhatHeThong import DTODanhSachPhatHeThong
from DTO.DTOBaiHat import DTOBaiHat
from datetime import datetime, date

class DALQuanLyDanhSachPhatHeThong:
    def __init__(self):
        super().__init__()
        # Khởi tạo database
        self.db = Database()  
        self.connection = self.db.connection
        self.cursor = self.db.cursor
        
    def them_nhac_chi_tiet_danh_sach_phat(self, ma_danh_sach_phat: int, ma_bai_hat: list):
        try:
            # Nếu ma_bai_hat là một số nguyên đơn lẻ, chuyển thành list
            if isinstance(ma_bai_hat, int):
                ma_bai_hat = [ma_bai_hat]
            
            # Nếu không có bài hát để thêm
            if not ma_bai_hat or len(ma_bai_hat) == 0:
                print("Lỗi: Không có bài hát nào để thêm")
                return 0, 0
            
            # Đếm số lượng bài hát thêm thành công và thất bại
            success_count = 0
            failed_count = 0
            
            # Sử dụng executemany để thêm nhiều bài hát cùng lúc
            query = """
                INSERT INTO ChiTietDanhSachPhatHeThong(MaDanhSachPhatHeThong, MaBaiHat)
                VALUES(%s, %s)
            """
            
            # Chuẩn bị dữ liệu cho executemany
            data = [(ma_danh_sach_phat, mabh) for mabh in ma_bai_hat]
            
            try:
                # Thực hiện thêm nhiều bản ghi
                self.cursor.executemany(query, data)
                self.connection.commit()
                success_count = len(ma_bai_hat)
                print(f"Đã thêm thành công {success_count} bài hát vào danh sách phát {ma_danh_sach_phat}")
                return success_count, failed_count
            except Exception as batch_error:
                # Nếu thêm hàng loạt thất bại, thử thêm từng bài hát một
                print(f"Lỗi khi thêm hàng loạt: {batch_error}")
                print("Thử thêm từng bài hát một...")
                self.connection.rollback()
                
                # Thêm từng bài hát một
                for mabh in ma_bai_hat:
                    try:
                        # Kiểm tra xem bài hát đã tồn tại trong danh sách chưa
                        check_query = """
                            SELECT COUNT(*) as count
                            FROM ChiTietDanhSachPhatHeThong
                            WHERE MaDanhSachPhatHeThong = %s AND MaBaiHat = %s
                        """
                        self.cursor.execute(check_query, (ma_danh_sach_phat, mabh))
                        result = self.cursor.fetchone()
                        
                        if result and result["count"] > 0:
                            print(f"Bài hát có mã {mabh} đã tồn tại trong danh sách phát")
                            failed_count += 1
                            continue
                        
                        # Thêm bài hát mới
                        self.cursor.execute(query, (ma_danh_sach_phat, mabh))
                        self.connection.commit()
                        success_count += 1
                        print(f"Đã thêm bài hát có mã {mabh} vào danh sách phát {ma_danh_sach_phat}")
                    except Exception as single_error:
                        self.connection.rollback()
                        failed_count += 1
                        print(f"Lỗi khi thêm bài hát có mã {mabh}: {single_error}")
                
                return success_count, failed_count
        except Exception as e:
            self.connection.rollback()
            print(f"Lỗi khi thêm bài hát vào danh sách phát: {e}")
            import traceback
            traceback.print_exc()
            return 0, len(ma_bai_hat) if isinstance(ma_bai_hat, list) else 1
    
    def lay_bai_hat_chua_co_trong_danh_sach(self, ma_danh_sach_phat: int):
        try:
            query = """
                SELECT BH.MaBaiHat, BH.TieuDe, BH.AnhBaiHat, 
                    TH.MaCaSi, CS.TenCaSi 
                FROM BaiHat BH
                JOIN thuchien TH ON BH.MaBaiHat = TH.MaBaiHat
                JOIN CaSi CS ON TH.MaCaSi = CS.MaCaSi
                WHERE NOT EXISTS (
                    SELECT 1 
                    FROM ChiTietDanhSachPhatHeThong CT 
                    WHERE CT.MaBaiHat = BH.MaBaiHat 
                    AND CT.MaDanhSachPhatHeThong = %s
                )
                ORDER BY BH.TieuDe;
            """
            self.cursor.execute(query,(ma_danh_sach_phat,))
            rows = self.cursor.fetchall()
            
            if not rows:
                print("Không có bài hát nào chưa có trong danh sách phát hệ thống")
                return []
            
            if rows:
                # print("Các trường có sẵn trong kết quả truy vấn:")
                for key in rows[0].keys():
                    print(f"- {key}")
            
            bai_hat_dict = {}
            
            for row in rows:
                ma_bai_hat = row["MaBaiHat"]
                
                if ma_bai_hat not in bai_hat_dict:
                    bai_hat_dict[ma_bai_hat] = {
                        "MaBaiHat": ma_bai_hat,
                        "NgayPhatHanh": None,  # Không có trong truy vấn
                        "TieuDe": row["TieuDe"],
                        "Anh": row["AnhBaiHat"],  # Trường đã được đổi tên trong DB
                        "MaXuatXu": None,  # Không có trong truy vấn
                        "TenXuatXu": None,  # Không có trong truy vấn
                        "MaTheLoai": None,  # Không có trong truy vấn
                        "TenTheLoai": None,  # Không có trong truy vấn
                        "FileNhac": None,  # Không có trong truy vấn
                        "CaSi": []
                    }
                ca_si_info = {
                    "MaCaSi": row["MaCaSi"],
                    "TenCaSi": row["TenCaSi"]
                }
                # Kiểm tra xem ca sĩ đã tồn tại trong danh sách chưa
                if not any(cs["MaCaSi"] == ca_si_info["MaCaSi"] for cs in bai_hat_dict[ma_bai_hat]["CaSi"]):
                    bai_hat_dict[ma_bai_hat]["CaSi"].append(ca_si_info)
            # Chuyển đổi từ dictionary sang danh sách DTO
            danh_sach_bai_hat = []
            for bai_hat_data in bai_hat_dict.values():
                dto = DTOBaiHat(
                    MaBaiHat=bai_hat_data["MaBaiHat"],
                    NgayPhatHanh=bai_hat_data["NgayPhatHanh"],
                    TieuDe=bai_hat_data["TieuDe"],
                    Anh=bai_hat_data["Anh"],
                    MaXuatXu=bai_hat_data["MaXuatXu"],
                    TenXuatXu=bai_hat_data["TenXuatXu"],
                    MaTheLoai=bai_hat_data["MaTheLoai"],
                    TenTheLoai=bai_hat_data["TenTheLoai"],
                    FileNhac=bai_hat_data["FileNhac"],
                    CaSi=bai_hat_data["CaSi"]
                )
                danh_sach_bai_hat.append(dto)
            return danh_sach_bai_hat

        except Exception as e:
            print(f"Lỗi SQL: {e}")
            import traceback
            traceback.print_exc()
            return []
        
    def xoa_bai_hat_trong_danh_sach(self, id_danh_sach_phat: int, id_bai_hat: int):
        try:
            query = "DELETE FROM ChiTietDanhSachPhatHeThong WHERE MaDanhSachPhatHeThong = %s AND MaBaiHat = %s"
            
            self.cursor.execute(query, (id_danh_sach_phat, id_bai_hat))
            
            self.connection.commit()
            
            affected_rows = self.cursor.rowcount
            
            if affected_rows > 0:
                print(f"Đã xóa bài hát (ID: {id_bai_hat}) khỏi danh sách phát (ID: {id_danh_sach_phat})")
                return True
            else:
                print(f"Không tìm thấy bài hát (ID: {id_bai_hat}) trong danh sách phát (ID: {id_danh_sach_phat})")
                return False
            
        except Exception as e:
            print(f"Lỗi khi xóa bài hát khỏi danh sách phát: {e}")
            self.connection.rollback()
            return False
        
    def lay_bai_hat_theo_danh_sach_he_thong(self, id_danh_sach_phat: int):
        try:
            query = """
                SELECT TH.MaBaiHat, BH.TieuDe, BH.AnhBaiHat, TH.MaCaSi, CaSi.TenCaSi 
                FROM BaiHat BH 
                JOIN ChiTietDanhSachPhatHeThong CT ON BH.MaBaiHat = CT.MaBaiHat 
                JOIN DanhSachPhatHeThong DSP ON CT.MaDanhSachPhatHeThong = DSP.MaDanhSachPhatHeThong 
                JOIN thuchien TH ON TH.MaBaiHat = BH.MaBaiHat
                JOIN CaSi ON CaSi.MaCaSi = TH.MaCaSi
                WHERE DSP.MaDanhSachPhatHeThong = %s
            """
            self.cursor.execute(query, (id_danh_sach_phat,))
            rows = self.cursor.fetchall()
            
            if not rows:
                print(f"Không tìm thấy bài hát nào trong danh sách phát có ID = {id_danh_sach_phat}")
                return []
            
            # In ra tên các trường để debug
            if rows:
                print("Các trường có sẵn trong kết quả truy vấn:")
                for key in rows[0].keys():
                    print(f"- {key}")
            
            # Nhóm bài hát theo ID
            bai_hat_dict = {}
            
            for row in rows:
                ma_bai_hat = row["MaBaiHat"]
                
                # Nếu bài hát chưa tồn tại trong dictionary, thêm mới
                if ma_bai_hat not in bai_hat_dict:
                    bai_hat_dict[ma_bai_hat] = {
                        "MaBaiHat": ma_bai_hat,
                        "NgayPhatHanh": None,  # Không có trong truy vấn
                        "TieuDe": row["TieuDe"],
                        "Anh": row["AnhBaiHat"],  # Trường đã được đổi tên trong DB
                        "MaXuatXu": None,  # Không có trong truy vấn
                        "TenXuatXu": None,  # Không có trong truy vấn
                        "MaTheLoai": None,  # Không có trong truy vấn
                        "TenTheLoai": None,  # Không có trong truy vấn
                        "FileNhac": None,  # Không có trong truy vấn
                        "CaSi": []
                    }
                
                # Thêm ca sĩ vào danh sách ca sĩ của bài hát
                ca_si_info = {
                    "MaCaSi": row["MaCaSi"],
                    "TenCaSi": row["TenCaSi"]
                }
                
                # Kiểm tra xem ca sĩ đã tồn tại trong danh sách chưa
                if not any(cs["MaCaSi"] == ca_si_info["MaCaSi"] for cs in bai_hat_dict[ma_bai_hat]["CaSi"]):
                    bai_hat_dict[ma_bai_hat]["CaSi"].append(ca_si_info)
            
            # Chuyển đổi từ dictionary sang danh sách DTO
            danh_sach_bai_hat = []
            for bai_hat_data in bai_hat_dict.values():
                dto = DTOBaiHat(
                    MaBaiHat=bai_hat_data["MaBaiHat"],
                    NgayPhatHanh=bai_hat_data["NgayPhatHanh"],
                    TieuDe=bai_hat_data["TieuDe"],
                    Anh=bai_hat_data["Anh"],
                    MaXuatXu=bai_hat_data["MaXuatXu"],
                    TenXuatXu=bai_hat_data["TenXuatXu"],
                    MaTheLoai=bai_hat_data["MaTheLoai"],
                    TenTheLoai=bai_hat_data["TenTheLoai"],
                    FileNhac=bai_hat_data["FileNhac"],
                    CaSi=bai_hat_data["CaSi"]
                )
                danh_sach_bai_hat.append(dto)
            return danh_sach_bai_hat

        except Exception as e:
            print(f"Lỗi SQL: {e}")
            import traceback
            traceback.print_exc()
            return []
                
    def lay_danh_sach_phat_he_thong_bang_id(self, id_danh_sach_phat: int):
        try:
            query = "SELECT * FROM DanhSachPhatHeThong WHERE MaDanhSachPhatHeThong = %s"
            self.cursor.execute(query, (id_danh_sach_phat,))
            row = self.cursor.fetchone()
            
            if not row:
                print(f"Không tìm thấy danh sách phát hệ thống có ID = {id_danh_sach_phat}")
                return None
                
            ngay_tao = row["NgayTao"]
            trang_thai = row["TrangThai"]
            if trang_thai is None:
                trang_thai = True 
            else:
                trang_thai = bool(trang_thai)
            dto = DTODanhSachPhatHeThong(
                MaDanhSachPhatHeThong=row["MaDanhSachPhatHeThong"],
                TieuDe=row["TieuDe"],
                MoTa=row["MoTa"],
                NgayTao=ngay_tao,
                TrangThai=trang_thai,
                Anh=row["Anh"]
            )
            return dto

        except Exception as e:
            print(f"Lỗi SQL: {e}")
            return None
        
    def lay_danh_sach_phat_he_thong(self):
        try:
            query = "SELECT * FROM DanhSachPhatHeThong"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            if not rows:
                print("Không có dữ liệu trong bảng DanhSachPhatHeThong")
                return []
                
            danh_sach = []
            for row in rows:
                ngay_tao = row["NgayTao"]
                if isinstance(ngay_tao, (datetime, date)):
                    ngay_tao = ngay_tao
                trang_thai = row["TrangThai"]
                if trang_thai is None:
                    trang_thai = True 
                else:
                    trang_thai = bool(trang_thai)
                dto = DTODanhSachPhatHeThong(
                    MaDanhSachPhatHeThong=row["MaDanhSachPhatHeThong"],
                    TieuDe=row["TieuDe"],
                    MoTa=row["MoTa"],
                    NgayTao=ngay_tao,
                    TrangThai=bool(row["TrangThai"]),
                    Anh=row["Anh"]
                )
                danh_sach.append(dto)
                
                
            return danh_sach

        except Exception as e:
            print(f"Lỗi SQL: {e}")
            return []
    def cap_nhat_danh_sach_phat(self, danh_sach_data):
        try:
            # Kiểm tra dữ liệu đầu vào
            if not danh_sach_data or "MaDanhSachPhatHeThong" not in danh_sach_data:
                print("Lỗi: Thiếu thông tin cần thiết cho cập nhật danh sách phát")
                return False
                
            # In thông tin debug
            print(f"DAL - Cập nhật danh sách phát với dữ liệu: {danh_sach_data}")
            
            # Xác định tên trường ID chính xác
            id_field = "MaDanhSachPhatHeThong"  # Mặc định
            
            # Xây dựng các phần của câu truy vấn
            set_parts = []
            params = []
            
            # Tiêu đề
            if 'TieuDe' in danh_sach_data:
                set_parts.append("TieuDe = %s")
                params.append(danh_sach_data['TieuDe'])
            
            # Mô tả
            if 'MoTa' in danh_sach_data:
                set_parts.append("MoTa = %s")
                params.append(danh_sach_data['MoTa'])
            
            # Trạng thái
            if 'TrangThai' in danh_sach_data:
                set_parts.append("TrangThai = %s")
                params.append(danh_sach_data['TrangThai'])
            
            # Ảnh - xử lý đặc biệt cho trường hợp NULL
            if 'Anh' in danh_sach_data:
                if danh_sach_data['Anh'] is None:
                    set_parts.append("Anh = NULL")
                else:
                    set_parts.append("Anh = %s")
                    params.append(danh_sach_data['Anh'])
            
            # Kiểm tra xem có phần nào cần cập nhật không
            if not set_parts:
                print("DAL - Không có trường nào để cập nhật")
                return False
            
            # Tạo câu truy vấn SQL
            query = f"""
                UPDATE DanhSachPhatHeThong
                SET {', '.join(set_parts)}
                WHERE {id_field} = %s
            """
            
            # Thêm mã danh sách vào params
            params.append(danh_sach_data['MaDanhSachPhatHeThong'])
            
            # In câu truy vấn để debug
            print(f"DAL - Thực thi truy vấn: {query}")
            print(f"DAL - Với tham số: {params}")
            
            # Thực thi câu truy vấn
            self.cursor.execute(query, params)
            
            # Commit để lưu thay đổi
            self.connection.commit()
            
            # Kiểm tra số hàng bị ảnh hưởng
            affected_rows = self.cursor.rowcount
            print(f"DAL - Số hàng bị ảnh hưởng: {affected_rows}")
            
            # Trả về True nếu có ít nhất một hàng bị ảnh hưởng
            return affected_rows >=0
            
        except Exception as e:
            # In thông báo lỗi chi tiết
            print(f"DAL - Lỗi khi cập nhật danh sách phát: {str(e)}")
            
            # Nếu có connection, rollback để tránh transaction không hoàn thành
            if 'connection' in locals() and self.connection:
                self.connection.rollback()
                
            # Trả về False khi có lỗi
            return False
        
    def xoa_danh_sach_phat_he_thong(self, ma_danh_sach):
        try:
            # Kiểm tra tham số đầu vào
            if not ma_danh_sach:
                print("Lỗi: Không có mã danh sách phát hệ thống")
                return False
                
            print(f"Bắt đầu xóa danh sách phát hệ thống có mã {ma_danh_sach}...")
            
            # Kiểm tra kết nối
            if not self.connection:
                print("Lỗi: Không có kết nối đến cơ sở dữ liệu")
                return False
            
            # 1. Đầu tiên xóa tất cả chi tiết danh sách phát
            chi_tiet_query = """
                DELETE FROM ChiTietDanhSachPhatHeThong 
                WHERE MaDanhSachPhatHeThong = %s
            """
            self.cursor.execute(chi_tiet_query, (ma_danh_sach,))
            rows_chi_tiet = self.cursor.rowcount
            print(f"Đã xóa {rows_chi_tiet} bản ghi từ bảng ChiTietDanhSachPhatHeThong")
            
            # 2. Sau đó xóa danh sách phát
            danh_sach_query = """
                DELETE FROM DanhSachPhatHeThong 
                WHERE MaDanhSachPhatHeThong = %s
            """
            self.cursor.execute(danh_sach_query, (ma_danh_sach,))
            rows_danh_sach = self.cursor.rowcount
            print(f"Đã xóa {rows_danh_sach} bản ghi từ bảng DanhSachPhatHeThong")
            
            # Kiểm tra xem danh sách đã xóa chưa
            if rows_danh_sach == 0:
                print(f"Không tìm thấy danh sách phát hệ thống với mã {ma_danh_sach}")
                self.connection.rollback()
                return False
                
            # Commit các thay đổi
            self.connection.commit()
            print(f"Đã xóa thành công danh sách phát hệ thống có mã {ma_danh_sach} và {rows_chi_tiet} chi tiết liên quan")
            return True
            
        except Exception as e:
            # Rollback khi có lỗi
            if self.connection:
                self.connection.rollback()
            
            print(f"Lỗi khi xóa danh sách phát hệ thống: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
        
    def lay_id_max_danh_sach_phat_he_thong(self):
        try:
            # Kiểm tra kết nối
            if not self.connection:
                print("Lỗi: Không có kết nối đến cơ sở dữ liệu")
                return 0
            
            # Truy vấn lấy ID lớn nhất
            query = """
                SELECT MAX(MaDanhSachPhatHeThong) as MaxID 
                FROM DanhSachPhatHeThong
            """
            
            # Thực thi truy vấn
            self.cursor.execute(query)
            
            # Lấy kết quả
            result = self.cursor.fetchone()
            
            # Kiểm tra kết quả
            if result and result['MaxID'] is not None:
                max_id = result['MaxID']
                return max_id + 1
            else:
                print("Bảng DanhSachPhatHeThong không có dữ liệu")
                return 0
                
        except Exception as e:
            print(f"Lỗi khi lấy ID lớn nhất: {str(e)}")
            import traceback
            traceback.print_exc()
            
    def them_danh_sach_phat_he_thong_moi(self, data):
        try:
            # Kiểm tra kết nối
            if not self.connection:
                print("Lỗi: Không có kết nối đến cơ sở dữ liệu")
                return False
                
            # Chuẩn bị câu lệnh SQL
            query = """
                INSERT INTO DanhSachPhatHeThong(TieuDe, MoTa, NgayTao, TrangThai, Anh)
                VALUES(%s, %s, %s, %s, %s)
                """
                
            # Thực thi câu lệnh
            self.cursor.execute(query, (
                data["TieuDe"],
                data["MoTa"],
                data["NgayTao"],
                data["TrangThai"],
                data["Anh"]
            ))
            
            # Lấy ID của bản ghi vừa thêm
            new_id = self.cursor.lastrowid
            
            # Commit các thay đổi
            self.connection.commit()
            
            print(f"Đã thêm danh sách phát hệ thống mới thành công với ID: {new_id}")
            return new_id
            
        except Exception as e:
            # Rollback nếu có lỗi
            if self.connection:
                self.connection.rollback()
                
            print(f"Lỗi khi thêm danh sách phát hệ thống: {str(e)}")
            import traceback
            traceback.print_exc()
            return False