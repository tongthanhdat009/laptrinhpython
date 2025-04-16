-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th4 16, 2025 lúc 01:59 PM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.1.25

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
  `AnhBaiHat` varchar(255) DEFAULT NULL,
  `MaXuatXu` int(11) DEFAULT NULL,
  `MaTheLoai` int(11) DEFAULT NULL,
  `FileNhac` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `baihat`
--

INSERT INTO `baihat` (`MaBaiHat`, `NgayPhatHanh`, `TieuDe`, `AnhBaiHat`, `MaXuatXu`, `MaTheLoai`, `FileNhac`) VALUES
(1, '2017-01-01', 'Nơi Này Có Anh', '/assets/AnhBaiHat/1.png', 1, 1, '/assets/FileNhac/1.mp3'),
(2, '2018-05-01', 'Chạy Ngay Đi', '/assets/AnhBaiHat/2.png', 1, 1, '/assets/FileNhac/2.mp3'),
(3, '2019-03-01', 'Có Chắc Yêu Là Đây', '/assets/AnhBaiHat/3.png', 1, 1, '/assets/FileNhac/3.mp3'),
(4, '2020-01-01', 'Muộn Rồi Mà Sao Còn', '/assets/AnhBaiHat/4.png', 1, 1, '/assets/FileNhac/4.mp3'),
(5, '2021-06-01', 'Chúng Ta Không Thuộc Về Nhau', '/assets/AnhBaiHat/5.png', 1, 1, '/assets/FileNhac/5.mp3'),
(6, '2022-02-01', 'Cơn Mưa Ngang Qua', '/assets/AnhBaiHat/6.png', 1, 1, '/assets/FileNhac/6.mp3'),
(7, '2021-09-04', 'Không Phải Dạng Vừa Đâu', '/assets/AnhBaiHat/7.png', 1, 1, '/assets/FileNhac/7.mp3'),
(8, '2018-05-25', 'Hơn Cả Yêu', '/assets/AnhBaiHat/8.png', 1, 1, '/assets/FileNhac/8.mp3'),
(9, '2018-06-15', 'Ánh Nắng Của Anh', '/assets/AnhBaiHat/9.png', 1, 1, '/assets/FileNhac/9.mp3'),
(10, '2019-03-10', 'Cứ Yêu Đi', '/assets/AnhBaiHat/10.png', 1, 1, '/assets/FileNhac/10.mp3'),
(11, '2020-07-30', 'Ta Còn Yêu Nhau', '/assets/AnhBaiHat/11.png', 1, 1, '/assets/FileNhac/11.mp3'),
(12, '2021-04-18', 'Năm Ấy', '/assets/AnhBaiHat/12.png', 1, 1, '/assets/FileNhac/12.mp3'),
(13, '2017-07-01', 'Em Gái Mưa', '/assets/AnhBaiHat/13.png', 1, 1, '/assets/FileNhac/13.mp3'),
(14, '2017-08-01', 'Duyên Mình Lỡ', '/assets/AnhBaiHat/14.png', 1, 1, '/assets/FileNhac/14.mp3'),
(15, '2018-03-01', 'Cho Em Gần Anh Thêm Chút Nữa', '/assets/AnhBaiHat/15.png', 1, 1, '/assets/FileNhac/15.mp3'),
(21, '2019-08-10', 'Bài này chill phết', '/assets/AnhBaiHat/21.png', 1, 2, '/assets/FileNhac/21.mp3'),
(22, '2020-05-15', 'Lối nhỏ', '/assets/AnhBaiHat/22.png', 1, 2, '/assets/FileNhac/22.mp3'),
(23, '2021-04-01', 'Ngày khác lạ', '/assets/AnhBaiHat/23.png', 1, 2, '/assets/FileNhac/23.mp3'),
(24, '2021-06-30', 'Anh đếch cần gì nhiều ngoài em', '/assets/AnhBaiHat/24.png', 1, 2, '/assets/FileNhac/24.mp3'),
(25, '2022-02-20', 'Đưa nhau đi trốn', '/assets/AnhBaiHat/25.png', 1, 2, '/assets/FileNhac/25.mp3');

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
  `AnhCaSi` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `casi`
--

INSERT INTO `casi` (`MaCaSi`, `TenCaSi`, `NgheDanh`, `NgaySinh`, `MoTa`, `AnhCaSi`) VALUES
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

--
-- Đang đổ dữ liệu cho bảng `chitietdanhsachphat`
--

INSERT INTO `chitietdanhsachphat` (`MaBaiHat`, `MaDanhSachPhat`) VALUES
(2, 2);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `chitietdanhsachphathethong`
--

CREATE TABLE `chitietdanhsachphathethong` (
  `MaBaiHat` int(11) NOT NULL,
  `MaDanhSachPhatHeThong` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `chitietdanhsachphathethong`
--

INSERT INTO `chitietdanhsachphathethong` (`MaBaiHat`, `MaDanhSachPhatHeThong`) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1),
(9, 1),
(10, 1),
(11, 1),
(11, 2),
(12, 1),
(13, 1),
(14, 1),
(24, 1);

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
  `Anh` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `danhsachphat`
--

INSERT INTO `danhsachphat` (`MaDanhSachPhat`, `TieuDe`, `MoTa`, `NgayTao`, `MaNguoiDung`, `Anh`) VALUES
(1, 'nhac cua tui', '', '2025-04-16', 1, 'assets/DanhSachPhat/None.png'),
(2, 'nhac cua tui 2', '', '2025-04-16', 1, 'assets/DanhSachPhat/2.png');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `danhsachphathethong`
--

CREATE TABLE `danhsachphathethong` (
  `MaDanhSachPhatHeThong` int(11) NOT NULL,
  `TieuDe` varchar(255) DEFAULT NULL,
  `MoTa` varchar(255) DEFAULT NULL,
  `NgayTao` date DEFAULT NULL,
  `TrangThai` tinyint(1) NOT NULL DEFAULT 0,
  `Anh` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `danhsachphathethong`
--

INSERT INTO `danhsachphathethong` (`MaDanhSachPhatHeThong`, `TieuDe`, `MoTa`, `NgayTao`, `TrangThai`, `Anh`) VALUES
(1, '99%', 'Em xi cây', '2025-03-21', 0, 'assets\\DanhSachPhatHeThong\\1.jpg'),
(2, 'The Wxrdie', 'quá dữ', '2025-03-22', 0, 'assets\\DanhSachPhatHeThong\\2.png');

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

--
-- Đang đổ dữ liệu cho bảng `luotnghe`
--

INSERT INTO `luotnghe` (`MaLuotNghe`, `MaNguoiDung`, `MaBaiHat`, `ThoiGian`) VALUES
(1, 1, 1, '2025-04-16 18:14:36'),
(2, 1, 2, '2025-04-16 18:14:37'),
(3, 1, 1, '2025-04-16 18:42:08'),
(4, 1, 2, '2025-04-16 18:42:09'),
(5, 1, 3, '2025-04-16 18:42:09'),
(6, 1, 4, '2025-04-16 18:42:09'),
(7, 1, 4, '2025-04-16 18:42:10'),
(8, 1, 4, '2025-04-16 18:42:10'),
(9, 1, 4, '2025-04-16 18:42:10'),
(10, 1, 22, '2025-04-16 18:42:11'),
(11, 1, 4, '2025-04-16 18:42:13'),
(12, 1, 22, '2025-04-16 18:42:13'),
(13, 1, 4, '2025-04-16 18:42:13'),
(14, 1, 22, '2025-04-16 18:42:14'),
(15, 1, 4, '2025-04-16 18:42:14'),
(16, 1, 22, '2025-04-16 18:42:14'),
(17, 1, 4, '2025-04-16 18:42:15'),
(18, 1, 22, '2025-04-16 18:42:15'),
(19, 1, 4, '2025-04-16 18:42:15'),
(20, 1, 22, '2025-04-16 18:42:16'),
(21, 1, 4, '2025-04-16 18:42:16'),
(22, 1, 22, '2025-04-16 18:42:16'),
(23, 1, 4, '2025-04-16 18:42:17'),
(24, 1, 22, '2025-04-16 18:42:17'),
(25, 1, 4, '2025-04-16 18:42:17'),
(26, 1, 22, '2025-04-16 18:42:18'),
(27, 1, 4, '2025-04-16 18:42:18'),
(28, 1, 22, '2025-04-16 18:42:18'),
(29, 1, 4, '2025-04-16 18:42:19'),
(30, 1, 22, '2025-04-16 18:42:19'),
(31, 1, 4, '2025-04-16 18:42:19'),
(32, 1, 4, '2025-04-16 18:42:20'),
(33, 1, 4, '2025-04-16 18:42:20'),
(34, 1, 4, '2025-04-16 18:42:21'),
(35, 1, 4, '2025-04-16 18:42:21'),
(36, 1, 4, '2025-04-16 18:42:21'),
(37, 1, 4, '2025-04-16 18:42:22'),
(38, 1, 4, '2025-04-16 18:42:23'),
(39, 1, 4, '2025-04-16 18:42:23'),
(40, 1, 4, '2025-04-16 18:42:23'),
(41, 1, 4, '2025-04-16 18:42:24'),
(42, 1, 4, '2025-04-16 18:42:24'),
(43, 1, 4, '2025-04-16 18:42:25'),
(44, 1, 4, '2025-04-16 18:42:26'),
(45, 1, 4, '2025-04-16 18:42:27'),
(46, 1, 4, '2025-04-16 18:42:27'),
(47, 1, 4, '2025-04-16 18:42:27'),
(48, 1, 22, '2025-04-16 18:42:27'),
(49, 1, 4, '2025-04-16 18:42:28'),
(50, 1, 22, '2025-04-16 18:42:29'),
(51, 1, 4, '2025-04-16 18:42:29'),
(52, 1, 22, '2025-04-16 18:42:29'),
(53, 1, 4, '2025-04-16 18:42:30'),
(54, 1, 22, '2025-04-16 18:42:30'),
(55, 1, 1, '2025-04-16 18:43:57'),
(56, 1, 2, '2025-04-16 18:43:59'),
(57, 1, 3, '2025-04-16 18:43:59'),
(58, 1, 4, '2025-04-16 18:43:59'),
(59, 1, 4, '2025-04-16 18:44:00'),
(60, 1, 4, '2025-04-16 18:44:00'),
(61, 1, 4, '2025-04-16 18:44:00'),
(62, 1, 22, '2025-04-16 18:44:00'),
(63, 1, 4, '2025-04-16 18:44:01'),
(64, 1, 22, '2025-04-16 18:44:03'),
(65, 1, 4, '2025-04-16 18:44:03'),
(66, 1, 22, '2025-04-16 18:44:03'),
(67, 1, 4, '2025-04-16 18:44:04'),
(68, 1, 1, '2025-04-16 18:44:21'),
(69, 1, 2, '2025-04-16 18:44:22'),
(70, 1, 3, '2025-04-16 18:44:22'),
(71, 1, 4, '2025-04-16 18:44:22'),
(72, 1, 4, '2025-04-16 18:44:22'),
(73, 1, 4, '2025-04-16 18:44:22'),
(74, 1, 21, '2025-04-16 18:44:22'),
(75, 1, 22, '2025-04-16 18:44:22'),
(76, 1, 21, '2025-04-16 18:44:23'),
(77, 1, 22, '2025-04-16 18:44:24'),
(78, 1, 21, '2025-04-16 18:44:24'),
(79, 1, 22, '2025-04-16 18:44:24'),
(80, 1, 21, '2025-04-16 18:44:25'),
(81, 1, 22, '2025-04-16 18:44:25'),
(82, 1, 21, '2025-04-16 18:44:25'),
(83, 1, 22, '2025-04-16 18:44:25'),
(84, 1, 21, '2025-04-16 18:44:26'),
(85, 1, 22, '2025-04-16 18:44:26'),
(86, 1, 21, '2025-04-16 18:44:26'),
(87, 1, 22, '2025-04-16 18:44:27'),
(88, 1, 21, '2025-04-16 18:44:27'),
(89, 1, 22, '2025-04-16 18:44:27'),
(90, 1, 21, '2025-04-16 18:44:28'),
(91, 1, 22, '2025-04-16 18:44:28'),
(92, 1, 21, '2025-04-16 18:44:29'),
(93, 1, 4, '2025-04-16 18:44:29'),
(94, 1, 21, '2025-04-16 18:44:30'),
(95, 1, 4, '2025-04-16 18:44:30'),
(96, 1, 21, '2025-04-16 18:44:30'),
(97, 1, 4, '2025-04-16 18:44:30'),
(98, 1, 21, '2025-04-16 18:44:32'),
(99, 1, 22, '2025-04-16 18:44:32'),
(100, 1, 21, '2025-04-16 18:44:33'),
(101, 1, 22, '2025-04-16 18:44:33'),
(102, 1, 21, '2025-04-16 18:44:34'),
(103, 1, 22, '2025-04-16 18:44:34'),
(104, 1, 21, '2025-04-16 18:44:34'),
(105, 1, 22, '2025-04-16 18:44:35'),
(106, 1, 21, '2025-04-16 18:44:35'),
(107, 1, 4, '2025-04-16 18:44:36'),
(108, 1, 4, '2025-04-16 18:44:37'),
(109, 1, 4, '2025-04-16 18:44:37'),
(110, 1, 4, '2025-04-16 18:44:37'),
(111, 1, 4, '2025-04-16 18:44:38'),
(112, 1, 4, '2025-04-16 18:44:38'),
(113, 1, 4, '2025-04-16 18:44:39'),
(114, 1, 21, '2025-04-16 18:44:39'),
(115, 1, 22, '2025-04-16 18:44:39'),
(116, 1, 21, '2025-04-16 18:44:40'),
(117, 1, 22, '2025-04-16 18:44:40'),
(118, 1, 21, '2025-04-16 18:44:41'),
(119, 1, 22, '2025-04-16 18:44:41'),
(120, 1, 21, '2025-04-16 18:44:41'),
(121, 1, 4, '2025-04-16 18:44:42'),
(122, 1, 21, '2025-04-16 18:44:43'),
(123, 1, 4, '2025-04-16 18:44:43'),
(124, 1, 1, '2025-04-16 18:48:43'),
(125, 1, 1, '2025-04-16 18:53:32'),
(126, 1, 2, '2025-04-16 18:53:33'),
(127, 1, 3, '2025-04-16 18:53:34'),
(128, 1, 4, '2025-04-16 18:53:34'),
(129, 1, 4, '2025-04-16 18:53:34'),
(130, 1, 4, '2025-04-16 18:53:34'),
(131, 1, 21, '2025-04-16 18:53:35'),
(132, 1, 22, '2025-04-16 18:53:35'),
(133, 1, 2, '2025-04-16 18:55:02'),
(134, 1, 1, '2025-04-16 18:55:10'),
(135, 1, 1, '2025-04-16 18:55:17'),
(136, 1, 1, '2025-04-16 18:55:19'),
(137, 1, 2, '2025-04-16 18:55:19'),
(138, 1, 4, '2025-04-16 18:55:21'),
(139, 1, 3, '2025-04-16 18:55:22'),
(140, 1, 7, '2025-04-16 18:55:23'),
(141, 1, 7, '2025-04-16 18:55:24'),
(142, 1, 1, '2025-04-16 18:55:37'),
(143, 1, 2, '2025-04-16 18:55:38'),
(144, 1, 1, '2025-04-16 18:55:39'),
(145, 1, 1, '2025-04-16 18:57:17'),
(146, 1, 2, '2025-04-16 18:57:20'),
(147, 1, 3, '2025-04-16 18:57:22'),
(148, 1, 4, '2025-04-16 18:57:24'),
(149, 1, 5, '2025-04-16 18:57:25'),
(150, 1, 7, '2025-04-16 18:57:27'),
(151, 1, 8, '2025-04-16 18:57:30'),
(152, 1, 10, '2025-04-16 18:57:38'),
(153, 1, 11, '2025-04-16 18:57:41'),
(154, 1, 12, '2025-04-16 18:57:43');

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
  `MaYeuThich` int(11) NOT NULL,
  `MaNguoiDung` int(11) NOT NULL,
  `MaBaiHat` int(11) NOT NULL,
  `NgayThem` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `yeuthich`
--

INSERT INTO `yeuthich` (`MaYeuThich`, `MaNguoiDung`, `MaBaiHat`, `NgayThem`) VALUES
(1, 1, 2, '2025-04-16');

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
  ADD PRIMARY KEY (`MaYeuThich`),
  ADD KEY `MaNguoiDung` (`MaNguoiDung`),
  ADD KEY `MaBaiHat` (`MaBaiHat`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `baihat`
--
ALTER TABLE `baihat`
  MODIFY `MaBaiHat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT cho bảng `casi`
--
ALTER TABLE `casi`
  MODIFY `MaCaSi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT cho bảng `danhsachphat`
--
ALTER TABLE `danhsachphat`
  MODIFY `MaDanhSachPhat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `danhsachphathethong`
--
ALTER TABLE `danhsachphathethong`
  MODIFY `MaDanhSachPhatHeThong` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT cho bảng `luotnghe`
--
ALTER TABLE `luotnghe`
  MODIFY `MaLuotNghe` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=155;

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
-- AUTO_INCREMENT cho bảng `yeuthich`
--
ALTER TABLE `yeuthich`
  MODIFY `MaYeuThich` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

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
  ADD CONSTRAINT `yeuthich_ibfk_1` FOREIGN KEY (`MaNguoiDung`) REFERENCES `nguoidung` (`MaNguoiDung`),
  ADD CONSTRAINT `yeuthich_ibfk_2` FOREIGN KEY (`MaBaiHat`) REFERENCES `baihat` (`MaBaiHat`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
