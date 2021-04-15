-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 12, 2021 at 04:59 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ems`
--

-- --------------------------------------------------------

--
-- Table structure for table `emp_salary`
--

CREATE TABLE `emp_salary` (
  `e_id` int(11) NOT NULL,
  `designation` text NOT NULL,
  `name` text NOT NULL,
  `age` int(10) NOT NULL,
  `gender` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `hr_location` text NOT NULL,
  `doj` varchar(10) NOT NULL,
  `dob` varchar(10) NOT NULL,
  `experience` varchar(50) NOT NULL,
  `proof_id` varchar(50) NOT NULL,
  `contact` text NOT NULL,
  `status` text NOT NULL,
  `address` varchar(200) NOT NULL,
  `month` text NOT NULL,
  `year` text NOT NULL,
  `basic_salary` text NOT NULL,
  `t_days` text NOT NULL,
  `absent_days` text NOT NULL,
  `medical` text NOT NULL,
  `pf` text NOT NULL,
  `conveyance` text NOT NULL,
  `net_salary` text NOT NULL,
  `salary_receipt` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `emp_salary`
--

INSERT INTO `emp_salary` (`e_id`, `designation`, `name`, `age`, `gender`, `email`, `hr_location`, `doj`, `dob`, `experience`, `proof_id`, `contact`, `status`, `address`, `month`, `year`, `basic_salary`, `t_days`, `absent_days`, `medical`, `pf`, `conveyance`, `net_salary`, `salary_receipt`) VALUES
(1, 'CEO', 'Narendra Modi', 54, 'Male', 'modi@gmail.com', 'Gujrat', '21-05-1989', '10-08-1967', '32', '12567854', '5476185349', 'Married', 'Shanti Nagar,Vadodara,Gujrat\n', 'April', '2021', '500000', '31', '2', '3', '30000', '15000', '452738.94', '1.txt'),
(2, 'CIO', 'Amit Shah', 53, 'Male', 'shah@gmail.com', 'Mumbai', '23-04-1990', '15-02-1968', '31', '75346815', '6846318769', 'Married', 'Varsova,Mumbai,Maharashtra\n\n\n\n', 'May', '2020', '470000', '30', '1', '2000', '25000', '15000', '444331.33', '2.txt'),
(3, 'CTO', 'Ajit Doval', 52, 'Male', 'doval@gmail.com', 'Mumbai', '20-09-1990', '15-06-1969', '31', '78645135', '9571284384', 'Married', 'Kurla,Mumbai,Maharashtra\n', 'June', '2021', '490000', '31', '0', '0', '40000', '20000', '470000.0', '3.txt'),
(4, 'Chief Manager', 'Uddhav Thakre', 51, 'Male', 'thakre@gmail.com', 'Mumbai', '21-02-1992', '24-08-1970', '29', '45138195', '9510165421', 'Married', 'Matoshri Bunglow,Mumbai,Maharashtra\n', 'April', '2021', '450000', '30', '2', '1', '25000', '15000', '409999.0', '4.txt'),
(5, 'Account Manager', 'Ajit Pawar', 49, 'Male', 'pawar@gmail.com', 'Pune', '12-06-1993', '16-05-1972', '28', '83494687', '5943547156', 'Married', 'Baramati,Pune,Maharashtra\n', 'January', '2021', '330000', '31', '0', '0', '30000', '15000', '315000.0', '5.txt'),
(6, 'HR Manager', 'Dikshita Tripathi', 35, 'Female', 'trpathi@gmailcom', 'Rajasthan', '02-07-2001', '01-04-1986', '20', '49874615', '2045416544', 'Single', 'Bhavin Nagar,Rajasthan,India\n\n', 'February', '2021', '350000', '28', '5', '5', '20000', '10000', '277495.0', '6.txt'),
(7, 'Technical Manager ', 'Sanmesh Yashwantrao', 46, 'Male', 'yashwantrao@gmail.com', 'Mumbai', '08-03-2000', '21-08-1975', '21', '95764813', '8594671526', 'Single', 'Airoli,Mumbai,Maharashtra\n', 'April', '2021', '400000', '31', '0', '4', '15000', '10000', '394996.0', '7.txt'),
(8, 'Production Manager', 'Lokesh Shrikhande', 41, 'Male', 'shrikhande@gmail.com', 'Panvel', '01-06-2005', '03-04-1980', '16', '54841184', '8466141325', 'Married', 'Old Panvel,Near tehsil Office,Panvel,Maharashtra\n', 'Dec', '2021', '350000', '35', '4', '5', '6564', '6548', '309979.0', '8.txt'),
(9, 'Marketing Manager ', 'Shubham Vanage', 39, 'Male', 'vanage@gmail.com', 'Ambernath', '20-05-2004', '01-12-1982', '17', '94647456', '4132156456', 'Single', 'Ambernath,Thane,Maharashtara\n', 'November', '2021', '300000', '60', '6', '8', '15000', '7500', '262492.0', '9.txt'),
(10, 'Team Leader', 'Nishant Jadhav', 31, 'Male', 'jadhav@gmail.com', 'Panvel', '05-06-2008', '30-02-1990', '13', '76416747', '4672813181', 'Single', 'HDFC Circle,Panvel,Maharashtra\n', 'August', '2021', '150000', '56', '3', '2', '20000', '7500', '129462.29', '10.txt'),
(11, 'Employee', 'Sakshi Khaire', 29, 'Female', 'khaire@gamil.com', 'Navi Mumbai', '03-05-2010', '01-06-1992', '11', '64987111', '5456797745', 'Single', 'Airoli,Navi Mumbai,Maharashtra\n', 'February', '2021', '70000', '29', '0', '0', '8000', '5000', '67000.0', '11.txt'),
(12, 'Employee', 'Mansi Deshmukh', 29, 'Female', 'deshmukh@gmail.com', 'Mumbai', '20-05-2018', '18-05-1992', '3', '46544654', '4987448978', 'Single', 'Kalyan,Mumbai,Maharashtra\n', 'november', '2021', '50000', '30', '3', '0', '2500', '2000', '44500.0', '12.txt'),
(13, 'ML developer', 'Shivansh Mishra', 27, 'Male', 'mishra@gmail.com', 'UttarPradesh', '12-03-2018', '20-09-1994', '3', '16548964', '5444987489', 'Single', 'UttarPradesh,India	\n', 'September', '2021', '90000', '25', '2', '1', '4500', '2000', '80299.0', '13.txt'),
(14, 'Programmer', 'Pranit Patil', 27, 'Male', 'patil@gmail.com', 'Alibaug', '25-08-2015', '21-06-1994', '6', '97489616', '7464654598', 'Single', 'Alibaug,Raigad,Maharashtra\n', 'May', '2021', '80000', '31', '2', '0', '5000', '2000', '71838.71', '14.txt'),
(15, 'Coder', 'Drishti Rane', 23, 'Female', 'rane@gmail.com', 'Mumbai', '10-05-2019', '06-09-1998', '2', '84648956', '4834647463', 'Single', 'Andheri,Mumbai,Maharashtra\n\n', 'March', '2021', '50000', '30', '0', '0', '2000', '2000', '50000.0', '15.txt'),
(16, 'Junior Developer', 'Shruti More', 22, 'Female', 'more@gmail.com', 'Ratnagiri', '05-06-2020', '21-09-1999', '1', '14657983', '4564654486', 'Single', 'Devbaug,Ratnagiri,Maharashtra	\n', 'July', '2021', '30000', '30', '0', '0', '1500', '2000', '30500.0', '16.txt'),
(17, 'Interior Decorator', 'Damini Bhoir', 24, 'Female', 'bhoir@gmail.com', 'Navi Mumbai', '25-06-2018', '20-09-1997', '3', '41315418', '1546461654', 'Single', 'Nerul,Navi Mumbai,Maharashtra	\n', 'October', '2021', '60000', '38', '02', '2', '2500', '2000', '56340.11', '17.txt'),
(18, 'Coder', 'Darshana Singh', 26, 'Female', 'singh@gmail.com', 'Punjab', '04-08-2016', '02-08-1995', '5', '49765165', '8746548748', 'Married', 'Punjab,India\n', 'June', '2021', '60000', '56', '3', '0', '2300', '2500', '56985.71', '18.txt'),
(19, 'Coder', 'Harshali Thapa', 25, 'Female', 'singh@gmail.com', 'Kashmir', '04-08-2018', '02-08-1996', '3', '46132164', '4654746544', 'Married', 'Kashmir,India\n', 'June', '2021', '45000', '56', '3', '0', '2000', '2500', '43089.29', '19.txt'),
(20, 'Junior Developer', 'Shraddha Yadav', 25, 'Female', 'yadav@gmail.com', 'Bihar', '04-08-2017', '08-02-1996', '4', '56443156', '4545649660', 'Single', 'Bihar,India\n', 'July', '2021', '50000', '56', '2', '2', '2000', '2000', '48212.29', '20.txt'),
(21, 'Employee', 'Mayur Patil', 27, 'Male', 'mayur@gmail.com', 'Panvel', '01-02-2019', '25-04-1994', '2', '16741231', '1265464946', 'Single', 'Adaigaon,Panvel,Maharashtra\n\n', 'April', '2021', '45000', '31', '3', '2', '2500', '2000', '40143.16', '21.txt'),
(22, 'sdlknsdfl', 'sdfs', 0, 'srgr', 'rgrg', 'erer', 'lkjrgjlkdj', 'sdfkjnsd', 'srgsr', 'rrg', 'rgrege', 'rege', 'eree\n', 'ddec', '2021', '5000', '31', '2', '1', '200', '200', '4676.42', '22.txt'),
(24, 'ndkj', 'jiuhu', 0, 'ioh', 'hoh', 'ohioh', 'hhuioh', 'jbhjkcb', 'oihioh', 'hioho', 'o', 'ohj', 'oiho	hio	h\n', 'april', '2021', '45000', '31', '2', '2500', '2000', '3000', '40596.77', '24.txt');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `emp_salary`
--
ALTER TABLE `emp_salary`
  ADD PRIMARY KEY (`e_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `emp_salary`
--
ALTER TABLE `emp_salary`
  MODIFY `e_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=103;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
