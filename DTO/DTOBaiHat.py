import os
class DTOBaiHat:
    def __init__(self, MaBaiHat: int, NgayPhatHanh: str, TieuDe: str, Anh: str, MaXuatXu: int, TenXuatXu: str, MaTheLoai: int, TenTheLoai: str, FileNhac: str, CaSi: list):
        self.__MaBaiHat = MaBaiHat
        self.__NgayPhatHanh = NgayPhatHanh
        self.__TieuDe = TieuDe
        self.__Anh = Anh
        self.__MaXuatXu = MaXuatXu
        self.__TenXuatXu = TenXuatXu
        self.__MaTheLoai = MaTheLoai
        self.__TenTheLoai = TenTheLoai
        self.__FileNhac = FileNhac
        self.__CaSi = CaSi  # Danh sách ca sĩ (mảng)

    # Getter
    def getMaBaiHat(self):
        return self.__MaBaiHat

    def getNgayPhatHanh(self):
        return self.__NgayPhatHanh

    def getTieuDe(self):
        return self.__TieuDe

    def getAnh(self):
        return self.__Anh

    def getMaXuatXu(self):
        return self.__MaXuatXu

    def getTenXuatXu(self):
        return self.__TenXuatXu

    def getMaTheLoai(self):
        return self.__MaTheLoai

    def getTenTheLoai(self):
        return self.__TenTheLoai

    def getFileNhac(self):
        return self.__FileNhac

    def getCaSi(self):
        return self.__CaSi

    # Setter
    def setMaBaiHat(self, MaBaiHat: int):
        self.__MaBaiHat = MaBaiHat

    def setNgayPhatHanh(self, NgayPhatHanh: str):
        self.__NgayPhatHanh = NgayPhatHanh

    def setTieuDe(self, TieuDe: str):
        self.__TieuDe = TieuDe

    def setAnh(self, Anh: str):
        self.__Anh = Anh

    def setMaXuatXu(self, MaXuatXu: int):
        self.__MaXuatXu = MaXuatXu

    def setTenXuatXu(self, TenXuatXu: str):
        self.__TenXuatXu = TenXuatXu

    def setMaTheLoai(self, MaTheLoai: int):
        self.__MaTheLoai = MaTheLoai

    def setTenTheLoai(self, TenTheLoai: str):
        self.__TenTheLoai = TenTheLoai

    def setFileNhac(self, FileNhac: str):
        self.__FileNhac = FileNhac

    def setCaSi(self, CaSi: list):
        self.__CaSi = CaSi

    def check(self):
        errors = []

        # Kiểm tra tiêu đề bài hát
        if not isinstance(self.__TieuDe, str) or not (1 <= len(self.__TieuDe) <= 255):
            errors.append("Tên bài hát không hợp lệ! Độ dài phải từ 1-255 ký tự.")

        # Kiểm tra file ảnh
        valid_image_exts = {".jpg", ".jpeg", ".png", ".gif"}
        if not isinstance(self.__Anh, str) or os.path.splitext(self.__Anh)[1].lower() not in valid_image_exts:
            errors.append("Ảnh bìa không hợp lệ! Chỉ chấp nhận các định dạng: jpg, jpeg, png, gif.")

        # Kiểm tra file nhạc
        valid_audio_exts = {".mp3", ".wav", ".flac", ".aac"}
        if not isinstance(self.__FileNhac, str) or os.path.splitext(self.__FileNhac)[1].lower() not in valid_audio_exts:
            errors.append("File nhạc không hợp lệ! Chỉ chấp nhận các định dạng: mp3, wav, flac, aac.")

        # Kiểm tra danh sách ca sĩ
        if not isinstance(self.__CaSi, list) or not all(isinstance(ca_si, str) and ca_si for ca_si in self.__CaSi):
            errors.append("Danh sách ca sĩ không hợp lệ! Phải là một danh sách chứa tên ca sĩ hợp lệ.")

        return errors if errors else "Hợp lệ"
    