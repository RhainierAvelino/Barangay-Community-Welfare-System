-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 06, 2024 at 12:10 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `baranggaydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `assistance request`
--

CREATE TABLE `assistance request` (
  `request_id` int(64) NOT NULL,
  `resident_id` int(64) NOT NULL,
  `program_id` int(64) NOT NULL,
  `request_details` text NOT NULL,
  `request_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `assistance request`
--

INSERT INTO `assistance request` (`request_id`, `resident_id`, `program_id`, `request_details`, `request_date`, `status`) VALUES
(2, 1, 221, 'adasdsa', '2024-07-06 09:43:10', 'Pending');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `feedback_id` int(64) NOT NULL,
  `resident_id` int(64) NOT NULL,
  `feedback_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `feedback_text` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`feedback_id`, `resident_id`, `feedback_date`, `feedback_text`) VALUES
(2, 1, '0000-00-00 00:00:00', 'si nhier masyadong pogi kaya kukuha ako resources');

-- --------------------------------------------------------

--
-- Table structure for table `helpdesk`
--

CREATE TABLE `helpdesk` (
  `helpdesk_id` int(64) NOT NULL,
  `contact_type` varchar(255) NOT NULL,
  `contact_details` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `helpdesk`
--

INSERT INTO `helpdesk` (`helpdesk_id`, `contact_type`, `contact_details`) VALUES
(1, 'BFP-Emergency Contact', 'Phone: 729-5166, Email: BFP@yahoo.com\r\n\r\n\r\n'),
(2, 'MMDA- Emergency Contact', 'Phone: 882-4177, Email: MMDA@yahoo.com'),
(3, 'RED CROSS- Emergency Contact', 'Phone: 911-1876, Email: REDCROSS@yahoo.com'),
(4, 'PNP- Emergency Contact', 'Phone: 117, Email: PNPdistrict1@yahoo.com'),
(5, 'Barangay Official Emergency Contact', ' Phone: 09391286722');

-- --------------------------------------------------------

--
-- Table structure for table `resident`
--

CREATE TABLE `resident` (
  `resident_id` int(64) NOT NULL,
  `user_id` int(64) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `contact_number` varchar(50) NOT NULL,
  `date_of_birth` date NOT NULL,
  `gender` varchar(50) NOT NULL,
  `occupation` varchar(255) NOT NULL,
  `marital_status` varchar(50) NOT NULL,
  `household_income` decimal(64,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `resident`
--

INSERT INTO `resident` (`resident_id`, `user_id`, `full_name`, `address`, `contact_number`, `date_of_birth`, `gender`, `occupation`, `marital_status`, `household_income`) VALUES
(1, 2, 'John Mhike Delos Santos', 'sa tabing ilog', '096154823373', '0000-00-00', 'Male', 'snatcher', 'Single', 0),
(2, 2, 'carlito pelaez', 'biak na bato', '12312312', '0000-00-00', 'Male', 'asdasd', 'Single', 0),
(3, 2, 'asdasdas', 'asdasdas', '1213123', '0000-00-00', 'Male', 'sadasd', 'Single', 0),
(4, 4, 'asdasdas', '13213as', '211312312', '0000-00-00', 'Female', 'asdasd', 'Single', 10000);

-- --------------------------------------------------------

--
-- Table structure for table `resources`
--

CREATE TABLE `resources` (
  `resources_id` int(64) NOT NULL,
  `program_id` int(64) NOT NULL,
  `quantity` decimal(64,0) NOT NULL,
  `status` varchar(255) NOT NULL,
  `allocated_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `resources`
--

INSERT INTO `resources` (`resources_id`, `program_id`, `quantity`, `status`, `allocated_date`) VALUES
(580, 221, 2340000, 'Available', '2024-07-04 05:37:50'),
(581, 222, 6123, 'Available', '2024-07-04 05:37:50'),
(583, 224, 1653, 'Available', '2024-07-04 05:38:56'),
(584, 225, 14267, 'Available', '2024-07-04 05:38:56');

-- --------------------------------------------------------

--
-- Table structure for table `roles table`
--

CREATE TABLE `roles table` (
  `role_id` int(64) NOT NULL,
  `role_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `roles table`
--

INSERT INTO `roles table` (`role_id`, `role_name`) VALUES
(1, '[admin]'),
(2, '[user]');

-- --------------------------------------------------------

--
-- Table structure for table `socialwelfareprograms`
--

CREATE TABLE `socialwelfareprograms` (
  `program_id` int(64) NOT NULL,
  `program_name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `eligibility_criteria` text NOT NULL,
  `application_process` text NOT NULL,
  `contact_person` varchar(255) NOT NULL,
  `contact_number` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `socialwelfareprograms`
--

INSERT INTO `socialwelfareprograms` (`program_id`, `program_name`, `description`, `eligibility_criteria`, `application_process`, `contact_person`, `contact_number`) VALUES
(220, 'Others', 'None', 'None', 'None', 'None', 'None'),
(221, 'Medical Supplies', 'Provides financial help for medical expenses', 'Low income, medical emergency', 'Submit medical records and/or doctor’s prescription ', 'Dr. Smith', '0906-045-2101'),
(222, 'School Supplies', 'School supplies for students.', 'Low income, enrolled in school', 'Submit school enrollment and grades not less than the average of 85%', 'Ms. Ramos', '0917-000-1002'),
(224, 'Health and Hygiene Kits', 'Kits containing hygiene and health products.', 'Low income, barangay resident', 'Register at barangay hall', 'Mr. Cruz', '0956-234-5003'),
(225, 'Relief Goods', 'Food packs for low-income families.', 'Low income, barangay resident', 'Submit Indigency', 'Ms. Lopez', '0923-481-2004');

-- --------------------------------------------------------

--
-- Table structure for table `users table`
--

CREATE TABLE `users table` (
  `user_id` int(64) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role_id` int(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users table`
--

INSERT INTO `users table` (`user_id`, `username`, `password`, `role_id`) VALUES
(1, 'admin', '777', 1),
(2, 'mhike', '123', 2),
(3, 'mhike', '1231', 2),
(4, 'sadasd', '123', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `assistance request`
--
ALTER TABLE `assistance request`
  ADD PRIMARY KEY (`request_id`) USING BTREE,
  ADD KEY `program_id` (`program_id`),
  ADD KEY `resident_id` (`resident_id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`feedback_id`),
  ADD KEY `resident_id` (`resident_id`);

--
-- Indexes for table `helpdesk`
--
ALTER TABLE `helpdesk`
  ADD PRIMARY KEY (`helpdesk_id`);

--
-- Indexes for table `resident`
--
ALTER TABLE `resident`
  ADD PRIMARY KEY (`resident_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `resources`
--
ALTER TABLE `resources`
  ADD PRIMARY KEY (`resources_id`),
  ADD KEY `program_id` (`program_id`);

--
-- Indexes for table `roles table`
--
ALTER TABLE `roles table`
  ADD PRIMARY KEY (`role_id`);

--
-- Indexes for table `socialwelfareprograms`
--
ALTER TABLE `socialwelfareprograms`
  ADD PRIMARY KEY (`program_id`);

--
-- Indexes for table `users table`
--
ALTER TABLE `users table`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `assistance request`
--
ALTER TABLE `assistance request`
  MODIFY `request_id` int(64) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `feedback_id` int(64) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `helpdesk`
--
ALTER TABLE `helpdesk`
  MODIFY `helpdesk_id` int(64) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `resident`
--
ALTER TABLE `resident`
  MODIFY `resident_id` int(64) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `resources`
--
ALTER TABLE `resources`
  MODIFY `resources_id` int(64) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=585;

--
-- AUTO_INCREMENT for table `roles table`
--
ALTER TABLE `roles table`
  MODIFY `role_id` int(64) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `socialwelfareprograms`
--
ALTER TABLE `socialwelfareprograms`
  MODIFY `program_id` int(64) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=227;

--
-- AUTO_INCREMENT for table `users table`
--
ALTER TABLE `users table`
  MODIFY `user_id` int(64) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `assistance request`
--
ALTER TABLE `assistance request`
  ADD CONSTRAINT `assistance request_ibfk_1` FOREIGN KEY (`program_id`) REFERENCES `socialwelfareprograms` (`program_id`),
  ADD CONSTRAINT `assistance request_ibfk_2` FOREIGN KEY (`resident_id`) REFERENCES `resident` (`resident_id`);

--
-- Constraints for table `feedback`
--
ALTER TABLE `feedback`
  ADD CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`resident_id`) REFERENCES `resident` (`resident_id`);

--
-- Constraints for table `resident`
--
ALTER TABLE `resident`
  ADD CONSTRAINT `resident_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users table` (`user_id`);

--
-- Constraints for table `resources`
--
ALTER TABLE `resources`
  ADD CONSTRAINT `resources_ibfk_1` FOREIGN KEY (`program_id`) REFERENCES `socialwelfareprograms` (`program_id`);

--
-- Constraints for table `users table`
--
ALTER TABLE `users table`
  ADD CONSTRAINT `users table_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles table` (`role_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
