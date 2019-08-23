-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 23, 2019 at 10:19 AM
-- Server version: 5.7.27-0ubuntu0.18.04.1
-- PHP Version: 7.3.8-1+ubuntu18.04.1+deb.sury.org+1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `university`
--

-- --------------------------------------------------------

--
-- Table structure for table `mark`
--

CREATE TABLE `mark` (
  `id` int(11) NOT NULL,
  `subj` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `mark` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `mark`
--

INSERT INTO `mark` (`id`, `subj`, `mark`, `user_id`) VALUES
(1, 'Физика', 5, 7),
(2, 'Физика', 4, 6),
(3, 'Хімія', 5, 6),
(4, 'Хімія', 4, 8),
(5, 'Хімія', 4, 7),
(12, 'Теологія', 3, 6),
(13, 'Філософія', 4, 6),
(14, 'Співи', 5, 6),
(15, 'Теологія', 3, 7),
(16, 'Філософія', 3, 7),
(17, 'Теологія', 5, 10),
(18, 'Філософія', 4, 10),
(19, 'Теологія', 4, 9),
(20, 'Філософія', 5, 9),
(21, 'Теологія', 2, 11),
(22, 'Філософія', 5, 11),
(23, 'Біологія', 3, 11),
(24, 'Філософія', 2, 12),
(25, 'Біологія', 4, 12);

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `second_name` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `s_group` int(11) NOT NULL,
  `number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `name`, `second_name`, `s_group`, `number`) VALUES
(6, 'Tolik', 'Shevchenko', 4, 134542),
(7, 'Ivan', 'Ivanov', 5, 165489),
(8, 'Микола', 'Дяченко', 4, 84384834),
(9, 'Денис', 'Вовк', 5, 445874),
(10, 'Александр', 'Пупа', 8, 78512),
(11, 'Александр', 'Лупа', 6, 32442),
(12, 'Микола', 'Погода', 7, 2342);

-- --------------------------------------------------------

--
-- Table structure for table `s_group`
--

CREATE TABLE `s_group` (
  `id` int(11) NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `faculty` varchar(30) COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `s_group`
--

INSERT INTO `s_group` (`id`, `name`, `faculty`) VALUES
(4, 'Fk-12', 'Медичний'),
(5, 'RT-12', 'Радіотех'),
(6, 'м-22', 'Медичний'),
(7, 'го-44', 'Маркетинг'),
(8, 'CCNA', 'Інженерно Фізичний Факультет');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(30) COLLATE utf8mb4_bin NOT NULL,
  `password` varchar(30) COLLATE utf8mb4_bin NOT NULL,
  `isadmin` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `isadmin`) VALUES
(1, 'admin', 'adminpass', 1),
(2, 'user', 'user', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mark`
--
ALTER TABLE `mark`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mark_rel` (`user_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `number` (`number`),
  ADD KEY `gropup_rel` (`s_group`);

--
-- Indexes for table `s_group`
--
ALTER TABLE `s_group`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mark`
--
ALTER TABLE `mark`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `s_group`
--
ALTER TABLE `s_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `mark`
--
ALTER TABLE `mark`
  ADD CONSTRAINT `mark_rel` FOREIGN KEY (`user_id`) REFERENCES `students` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `students`
--
ALTER TABLE `students`
  ADD CONSTRAINT `gropup_rel` FOREIGN KEY (`s_group`) REFERENCES `s_group` (`id`) ON DELETE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
