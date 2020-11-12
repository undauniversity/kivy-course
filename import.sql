-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: sql101.epizy.com
-- Waktu pembuatan: 11 Nov 2020 pada 09.57
-- Versi server: 5.6.21-69.0
-- Versi PHP: 7.2.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `epiz_27024105_siakad`
--
CREATE DATABASE IF NOT EXISTS `epiz_27024105_siakad` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `epiz_27024105_siakad`;

-- --------------------------------------------------------

--
-- Struktur dari tabel `mahasiswa`
--

CREATE TABLE IF NOT EXISTS `mahasiswa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `npm` char(13) DEFAULT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `alamat` varchar(80) DEFAULT 'Sampit',
  PRIMARY KEY (`id`),
  UNIQUE KEY `npm` (`npm`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `mahasiswa`
--

INSERT INTO `mahasiswa` (`id`, `npm`, `nama`, `alamat`) VALUES
(1, '2057201000001', 'Palui', 'Jl Baamang'),
(2, '2057201000002', 'Galuh', 'Sampit'),
(4, '123', 'budi', 'Sampit'),
(5, '124', 'Arim', 'Sampit');

-- --------------------------------------------------------

--
-- Struktur dari tabel `matakuliah`
--

CREATE TABLE IF NOT EXISTS `matakuliah` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kodemk` char(5) NOT NULL,
  `nama_matakuliah` varchar(20) NOT NULL,
  `kelas` char(4) NOT NULL DEFAULT 'I-A',
  `Semester` char(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `kodemk` (`kodemk`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `matakuliah`
--

INSERT INTO `matakuliah` (`id`, `kodemk`, `nama_matakuliah`, `kelas`, `Semester`) VALUES
(1, 'MK123', 'Pemrog Andro', '7-C', '7'),
(2, 'MK124', 'Dasar Pemrog', 'I-A', '1'),
(3, 'MK111', 'bahasa', 'I-A', '1'),
(4, 'MK222', 'alpro', 'I-A', '1'),
(5, 'MK333', 'pkn', 'I-A', '1'),
(7, '777', 'agama', 'I-A', '1');
COMMIT;
