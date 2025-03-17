-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th3 17, 2025 lúc 03:29 PM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `phatnhac`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `baihat`
--

CREATE TABLE `baihat` (
  `MaBaiHat` int(11) NOT NULL,
  `NgayPhatHanh` date DEFAULT NULL,
  `TieuDe` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Anh` varchar(255) DEFAULT NULL,
  `MaXuatXu` int(11) DEFAULT NULL,
  `MaTheLoai` int(11) DEFAULT NULL,
  `FileNhac` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `baihat`
--

INSERT INTO `baihat` (`MaBaiHat`, `NgayPhatHanh`, `TieuDe`, `Anh`, `MaXuatXu`, `MaTheLoai`, `FileNhac`) VALUES
(1, '2017-01-01', 'Nơi Này Có Anh', '..\\assets\\AnhBaiHat\\1.png', 1, 1, '..\\assets\\FileNhac\\1.mp3'),
(2, '2018-05-01', 'Chạy Ngay Đi', '..\\assets\\AnhBaiHat\\2.png', 1, 1, '..\\assets\\FileNhac\\2.mp3'),
(3, '2019-03-01', 'Có Chắc Yêu Là Đây', '..\\assets\\AnhBaiHat\\3.png', 1, 1, '..\\assets\\FileNhac\\3.mp3'),
(4, '2020-01-01', 'Muộn Rồi Mà Sao Còn', '..\\assets\\AnhBaiHat\\4.png', 1, 1, '..\\assets\\FileNhac\\4.mp3'),
(5, '2021-06-01', 'Chúng Ta Không Thuộc Về Nhau', '..\\assets\\AnhBaiHat\\5.png', 1, 1, '..\\assets\\FileNhac\\5.mp3'),
(6, '2022-02-01', 'Cơn Mưa Ngang Qua', '..\\assets\\AnhBaiHat\\6.png', 1, 1, '..\\assets\\FileNhac\\6.mp3'),
(7, '2021-09-04', 'Không Phải Dạng Vừa Đâu', '..\\assets\\AnhBaiHat\\7.png', 1, 1, '..\\assets\\FileNhac\\7.mp3'),
(8, '2018-05-25', 'Hơn Cả Yêu', '..\\assets\\AnhBaiHat\\8.png', 1, 1, '..\\assets\\FileNhac\\8.mp3'),
(9, '2018-06-15', 'Ánh Nắng Của Anh', '..\\assets\\AnhBaiHat\\9.png', 1, 1, '..\\assets\\FileNhac\\9.mp3'),
(10, '2019-03-10', 'Cứ Yêu Đi', '..\\assets\\AnhBaiHat\\10.png', 1, 1, '..\\assets\\FileNhac\\10.mp3'),
(11, '2020-07-30', 'Ta Còn Yêu Nhau', '..\\assets\\AnhBaiHat\\11.png', 1, 1, '..\\assets\\FileNhac\\11.mp3'),
(12, '2021-04-18', 'Năm Ấy', '..\\assets\\AnhBaiHat\\12.png', 1, 1, '..\\assets\\FileNhac\\12.mp3'),
(13, '2017-07-01', 'Em Gái Mưa', '..\\assets\\AnhBaiHat\\13.png', 1, 1, '..\\assets\\FileNhac\\13.mp3'),
(14, '2017-08-01', 'Duyên Mình Lỡ', '..\\assets\\AnhBaiHat\\14.png', 1, 1, '..\\assets\\FileNhac\\14.mp3'),
(15, '2018-03-01', 'Cho Em Gần Anh Thêm Chút Nữa', '..\\assets\\AnhBaiHat\\15.png', 1, 1, '..\\assets\\FileNhac\\15.mp3'),
(21, '2019-08-10', 'Bài này chill phết', '..\\assets\\AnhBaiHat\\21.png', 1, 2, '..\\assets\\FileNhac\\21.mp3'),
(22, '2020-05-15', 'Lối nhỏ', '..\\assets\\AnhBaiHat\\22.png', 1, 2, '..\\assets\\FileNhac\\22.mp3'),
(23, '2021-04-01', 'Ngày khác lạ', '..\\assets\\AnhBaiHat\\23.png', 1, 2, '..\\assets\\FileNhac\\23.mp3'),
(24, '2021-06-30', 'Anh đếch cần gì nhiều ngoài em', '..\\assets\\AnhBaiHat\\24.png', 1, 2, '..\\assets\\FileNhac\\24.mp3'),
(25, '2022-02-20', 'Đưa nhau đi trốn', '..\\assets\\AnhBaiHat\\25.png', 1, 2, '..\\assets\\FileNhac\\25.mp3');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `casi`
--

CREATE TABLE `casi` (
  `MaCaSi` int(11) NOT NULL,
  `TenCaSi` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `NgheDanh` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `NgaySinh` date DEFAULT NULL,
  `MoTa` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Anh` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `casi`
--

INSERT INTO `casi` (`MaCaSi`, `TenCaSi`, `NgheDanh`, `NgaySinh`, `MoTa`, `Anh`) VALUES
(1, 'Sơn Tùng M-TP', 'Sơn Tùng M-TP', '1994-07-05', 'Ca sĩ, nhạc sĩ nổi tiếng với nhiều ca khúc hit.', '..\\assets\\CaSi\\1.png'),
(2, 'Đức Phúc', 'Đức Phúc', '1996-10-19', 'Ca sĩ nổi bật với giọng hát mạnh mẽ và các ca khúc yêu thích.', '..\\assets\\CaSi\\2.png'),
(3, 'Hương Tràm', 'Hương Tràm', '1995-05-10', 'Ca sĩ nổi bật với giọng hát đầy cảm xúc và các bài hit.', '..\\assets\\CaSi\\3.png'),
(4, 'Min', 'Min', '1990-06-20', 'Ca sĩ trẻ trung, nổi bật với các bài hát pop.', '..\\assets\\CaSi\\4.png'),
(5, 'Erik', 'Erik', '1997-10-13', 'Ca sĩ với phong cách âm nhạc hiện đại và các ca khúc được yêu thích.', '..\\assets\\CaSi\\5.png'),
(6, 'Đen Vâu', 'Đen', '1989-05-13', 'Đen Vâu là một trong những ca sĩ, rapper nổi bật của Việt Nam, với phong cách âm nhạc đặc trưng và lời rap sâu sắc.', '..\\assets\\CaSi\\6.png');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `chitietdanhsachphat`
--

CREATE TABLE `chitietdanhsachphat` (
  `MaBaiHat` int(11) NOT NULL,
  `MaDanhSachPhat` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `chitietdanhsachphathethong`
--

CREATE TABLE `chitietdanhsachphathethong` (
  `MaBaiHat` int(11) NOT NULL,
  `MaDanhSachPhatHeThong` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `danhsachphat`
--

CREATE TABLE `danhsachphat` (
  `MaDanhSachPhat` int(11) NOT NULL,
  `TieuDe` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `MoTa` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `NgayTao` date DEFAULT NULL,
  `MaNguoiDung` int(11) DEFAULT NULL,
  `Anh` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `danhsachphathethong`
--

CREATE TABLE `danhsachphathethong` (
  `MaDanhSachPhatHeThong` int(11) NOT NULL,
  `TieuDe` varchar(255) DEFAULT NULL,
  `MoTa` varchar(255) DEFAULT NULL,
  `NgayTao` date DEFAULT NULL,
  `Anh` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `lichsutimkiem`
--

CREATE TABLE `lichsutimkiem` (
  `MaLichSu` int(11) NOT NULL,
  `NoiDung` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `MaNguoiDung` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `luotnghe`
--

CREATE TABLE `luotnghe` (
  `MaLuotNghe` int(11) NOT NULL,
  `MaNguoiDung` int(11) DEFAULT NULL,
  `MaBaiHat` int(11) DEFAULT NULL,
  `ThoiGian` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `nguoidung`
--

CREATE TABLE `nguoidung` (
  `MaNguoiDung` int(11) NOT NULL,
  `TenNguoiDung` varchar(255) DEFAULT NULL,
  `TaiKhoan` varchar(255) DEFAULT NULL,
  `MatKhau` varchar(255) NOT NULL,
  `MaQuyen` int(11) NOT NULL,
  `Anh` mediumblob DEFAULT NULL,
  `HoatDong` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `nguoidung`
--

INSERT INTO `nguoidung` (`MaNguoiDung`, `TenNguoiDung`, `TaiKhoan`, `MatKhau`, `MaQuyen`, `Anh`, `HoatDong`) VALUES
(1, 'admin', 'admin', 'admin', 1, NULL, 0);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `quyen`
--

CREATE TABLE `quyen` (
  `MaQuyen` int(11) NOT NULL,
  `TenQuyen` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `quyen`
--

INSERT INTO `quyen` (`MaQuyen`, `TenQuyen`) VALUES
(1, 'admin'),
(2, 'user');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `theloai`
--

CREATE TABLE `theloai` (
  `MaTheLoai` int(11) NOT NULL,
  `TenTheLoai` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `Anh` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `theloai`
--

INSERT INTO `theloai` (`MaTheLoai`, `TenTheLoai`, `Anh`) VALUES
(1, 'Pop', NULL),
(2, 'Rap/Hip-Hop', NULL),
(3, 'R&B', NULL),
(4, 'Dance/EDM', NULL),
(5, 'Ballad', NULL),
(6, 'Trữ Tình', NULL),
(7, 'Dân Ca', NULL),
(8, 'Rock', NULL),
(9, 'Bolero', NULL),
(10, 'Nhạc Thiếu Nhi', NULL);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `thuchien`
--

CREATE TABLE `thuchien` (
  `MaBaiHat` int(11) NOT NULL,
  `MaCaSi` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `thuchien`
--

INSERT INTO `thuchien` (`MaBaiHat`, `MaCaSi`) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 2),
(9, 2),
(10, 2),
(11, 2),
(12, 2),
(13, 3),
(14, 3),
(15, 3),
(21, 4),
(21, 6),
(22, 6),
(23, 6),
(24, 6),
(25, 6);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `xuatxu`
--

CREATE TABLE `xuatxu` (
  `MaXuatXu` int(11) NOT NULL,
  `TenXuatXu` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `xuatxu`
--

INSERT INTO `xuatxu` (`MaXuatXu`, `TenXuatXu`) VALUES
(1, 'Việt Nam'),
(2, 'Hàn Quốc'),
(3, 'US-UK');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `yeuthich`
--

CREATE TABLE `yeuthich` (
  `MaNguoiDung` int(11) NOT NULL,
  `MaBaiHat` int(11) NOT NULL,
  `NgayThem` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `baihat`
--
ALTER TABLE `baihat`
  ADD PRIMARY KEY (`MaBaiHat`),
  ADD KEY `MaXuatXu` (`MaXuatXu`),
  ADD KEY `FK_BaiHat_TheLoai` (`MaTheLoai`);

--
-- Chỉ mục cho bảng `casi`
--
ALTER TABLE `casi`
  ADD PRIMARY KEY (`MaCaSi`);

--
-- Chỉ mục cho bảng `chitietdanhsachphat`
--
ALTER TABLE `chitietdanhsachphat`
  ADD PRIMARY KEY (`MaBaiHat`,`MaDanhSachPhat`),
  ADD KEY `FK_ChiTietDanhSachPhat_DanhSachPhat` (`MaDanhSachPhat`);

--
-- Chỉ mục cho bảng `chitietdanhsachphathethong`
--
ALTER TABLE `chitietdanhsachphathethong`
  ADD PRIMARY KEY (`MaBaiHat`,`MaDanhSachPhatHeThong`),
  ADD KEY `MaDanhSachPhatHeThong` (`MaDanhSachPhatHeThong`);

--
-- Chỉ mục cho bảng `danhsachphat`
--
ALTER TABLE `danhsachphat`
  ADD PRIMARY KEY (`MaDanhSachPhat`),
  ADD KEY `FK_DanhSachPhat_NguoiDung` (`MaNguoiDung`);

--
-- Chỉ mục cho bảng `danhsachphathethong`
--
ALTER TABLE `danhsachphathethong`
  ADD PRIMARY KEY (`MaDanhSachPhatHeThong`);

--
-- Chỉ mục cho bảng `lichsutimkiem`
--
ALTER TABLE `lichsutimkiem`
  ADD PRIMARY KEY (`MaLichSu`),
  ADD KEY `FK_LichSuTimKiem_NguoiDung` (`MaNguoiDung`);

--
-- Chỉ mục cho bảng `luotnghe`
--
ALTER TABLE `luotnghe`
  ADD PRIMARY KEY (`MaLuotNghe`),
  ADD KEY `FK_LuotNghe_NguoiDung` (`MaNguoiDung`),
  ADD KEY `FK_LuotNghe_BaiHat` (`MaBaiHat`);

--
-- Chỉ mục cho bảng `nguoidung`
--
ALTER TABLE `nguoidung`
  ADD PRIMARY KEY (`MaNguoiDung`),
  ADD UNIQUE KEY `TaiKhoan` (`TaiKhoan`),
  ADD KEY `FK_NguoiDung_Quyen` (`MaQuyen`);

--
-- Chỉ mục cho bảng `quyen`
--
ALTER TABLE `quyen`
  ADD PRIMARY KEY (`MaQuyen`);

--
-- Chỉ mục cho bảng `theloai`
--
ALTER TABLE `theloai`
  ADD PRIMARY KEY (`MaTheLoai`);

--
-- Chỉ mục cho bảng `thuchien`
--
ALTER TABLE `thuchien`
  ADD PRIMARY KEY (`MaBaiHat`,`MaCaSi`),
  ADD KEY `MaCaSi` (`MaCaSi`);

--
-- Chỉ mục cho bảng `xuatxu`
--
ALTER TABLE `xuatxu`
  ADD PRIMARY KEY (`MaXuatXu`);

--
-- Chỉ mục cho bảng `yeuthich`
--
ALTER TABLE `yeuthich`
  ADD PRIMARY KEY (`MaNguoiDung`,`MaBaiHat`),
  ADD KEY `FK_YeuThich_BaiHat` (`MaBaiHat`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `baihat`
--
ALTER TABLE `baihat`
  MODIFY `MaBaiHat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT cho bảng `casi`
--
ALTER TABLE `casi`
  MODIFY `MaCaSi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT cho bảng `danhsachphat`
--
ALTER TABLE `danhsachphat`
  MODIFY `MaDanhSachPhat` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `danhsachphathethong`
--
ALTER TABLE `danhsachphathethong`
  MODIFY `MaDanhSachPhatHeThong` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `nguoidung`
--
ALTER TABLE `nguoidung`
  MODIFY `MaNguoiDung` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `quyen`
--
ALTER TABLE `quyen`
  MODIFY `MaQuyen` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `theloai`
--
ALTER TABLE `theloai`
  MODIFY `MaTheLoai` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT cho bảng `xuatxu`
--
ALTER TABLE `xuatxu`
  MODIFY `MaXuatXu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `baihat`
--
ALTER TABLE `baihat`
  ADD CONSTRAINT `FK_BaiHat_TheLoai` FOREIGN KEY (`MaTheLoai`) REFERENCES `theloai` (`MaTheLoai`),
  ADD CONSTRAINT `baihat_ibfk_1` FOREIGN KEY (`MaXuatXu`) REFERENCES `xuatxu` (`MaXuatXu`) ON DELETE SET NULL;

--
-- Các ràng buộc cho bảng `chitietdanhsachphat`
--
ALTER TABLE `chitietdanhsachphat`
  ADD CONSTRAINT `FK_ChiTietDanhSachPhat_BaiHat` FOREIGN KEY (`MaBaiHat`) REFERENCES `baihat` (`MaBaiHat`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ChiTietDanhSachPhat_DanhSachPhat` FOREIGN KEY (`MaDanhSachPhat`) REFERENCES `danhsachphat` (`MaDanhSachPhat`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Các ràng buộc cho bảng `chitietdanhsachphathethong`
--
ALTER TABLE `chitietdanhsachphathethong`
  ADD CONSTRAINT `chitietdanhsachphathethong_ibfk_1` FOREIGN KEY (`MaBaiHat`) REFERENCES `baihat` (`MaBaiHat`) ON DELETE CASCADE,
  ADD CONSTRAINT `chitietdanhsachphathethong_ibfk_2` FOREIGN KEY (`MaDanhSachPhatHeThong`) REFERENCES `danhsachphathethong` (`MaDanhSachPhatHeThong`) ON DELETE CASCADE;

--
-- Các ràng buộc cho bảng `danhsachphat`
--
ALTER TABLE `danhsachphat`
  ADD CONSTRAINT `FK_DanhSachPhat_NguoiDung` FOREIGN KEY (`MaNguoiDung`) REFERENCES `nguoidung` (`MaNguoiDung`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Các ràng buộc cho bảng `lichsutimkiem`
--
ALTER TABLE `lichsutimkiem`
  ADD CONSTRAINT `FK_LichSuTimKiem_NguoiDung` FOREIGN KEY (`MaNguoiDung`) REFERENCES `nguoidung` (`MaNguoiDung`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Các ràng buộc cho bảng `luotnghe`
--
ALTER TABLE `luotnghe`
  ADD CONSTRAINT `FK_LuotNghe_BaiHat` FOREIGN KEY (`MaBaiHat`) REFERENCES `baihat` (`MaBaiHat`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_LuotNghe_NguoiDung` FOREIGN KEY (`MaNguoiDung`) REFERENCES `nguoidung` (`MaNguoiDung`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Các ràng buộc cho bảng `nguoidung`
--
ALTER TABLE `nguoidung`
  ADD CONSTRAINT `FK_NguoiDung_Quyen` FOREIGN KEY (`MaQuyen`) REFERENCES `quyen` (`MaQuyen`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Các ràng buộc cho bảng `thuchien`
--
ALTER TABLE `thuchien`
  ADD CONSTRAINT `thuchien_ibfk_1` FOREIGN KEY (`MaBaiHat`) REFERENCES `baihat` (`MaBaiHat`) ON DELETE CASCADE,
  ADD CONSTRAINT `thuchien_ibfk_2` FOREIGN KEY (`MaCaSi`) REFERENCES `casi` (`MaCaSi`) ON DELETE CASCADE;

--
-- Các ràng buộc cho bảng `yeuthich`
--
ALTER TABLE `yeuthich`
  ADD CONSTRAINT `FK_YeuThich_BaiHat` FOREIGN KEY (`MaBaiHat`) REFERENCES `baihat` (`MaBaiHat`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_YeuThich_NguoiDung` FOREIGN KEY (`MaNguoiDung`) REFERENCES `nguoidung` (`MaNguoiDung`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
