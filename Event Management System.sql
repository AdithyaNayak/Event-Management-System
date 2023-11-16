CREATE database EVENT_MANAGEMENT_System;

use EVENT_MANAGEMENT_System;

-- Create tables
CREATE TABLE User (
    UserID INT PRIMARY KEY,
    Username VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Email VARCHAR(255),
    PhoneNo VARCHAR(20),
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Role VARCHAR(50) NOT NULL
);

CREATE TABLE Event (
    EventID INT PRIMARY KEY,
    EventName VARCHAR(255) NOT NULL,
    EventDescription TEXT,
    EventDate DATE,
    EventTime TIME,
    Location VARCHAR(255),
    MaxCapacity INT,
    EventType VARCHAR(50),
    EventStatus VARCHAR(50) NOT NULL
);

CREATE TABLE Participant (
    ParticipantID INT PRIMARY KEY,
    UserID INT,
    DateOfBirth DATE,
    PhoneNo VARCHAR(20),
    Address VARCHAR(255),
    PaymentInfo VARCHAR(255),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

CREATE TABLE EventFeedback (
    FeedbackID INT PRIMARY KEY,
    EventID INT,
    ParticipantID INT,
    Rating INT,
    Comments TEXT,
    FeedbackDate DATE,
    FOREIGN KEY (EventID) REFERENCES Event(EventID),
    FOREIGN KEY (ParticipantID) REFERENCES Participant(ParticipantID)
);

CREATE TABLE EventPlanner (
    PlannerID INT PRIMARY KEY,
    UserID INT,
    CompanyName VARCHAR(255),
    PhoneNo VARCHAR(20),
    EventsOrganized VARCHAR(255),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

CREATE TABLE Ticket (
    TicketID INT PRIMARY KEY,
    EventID INT,
    ParticipantID INT,
    TicketType VARCHAR(50) NOT NULL,
    TicketPrice DECIMAL(10,2) NOT NULL,
    PurchaseDate DATE,
    PaymentStatus VARCHAR(50) NOT NULL,
    FOREIGN KEY (EventID) REFERENCES Event(EventID),
    FOREIGN KEY (ParticipantID) REFERENCES Participant(ParticipantID)
);

CREATE TABLE AnalyticsData (
    AnalyticsID INT PRIMARY KEY,
    EventID INT,
    AttendanceCount INT,
    Revenue DECIMAL(10,2),
    ReportDate DATE,
    FOREIGN KEY (EventID) REFERENCES Event(EventID)
);

CREATE TABLE Ticketing (
    TicketingID INT PRIMARY KEY,
    EventID INT,
    ParticipantID INT,
    TicketID INT,
    FOREIGN KEY (EventID) REFERENCES Event(EventID),
    FOREIGN KEY (ParticipantID) REFERENCES Participant(ParticipantID),
    FOREIGN KEY (TicketID) REFERENCES Ticket(TicketID)
);

CREATE TABLE Feedback (
    FeedbackRelationshipID INT PRIMARY KEY,
    EventID INT,
    ParticipantID INT,
    FeedbackID INT,
    FOREIGN KEY (EventID) REFERENCES Event(EventID),
    FOREIGN KEY (ParticipantID) REFERENCES Participant(ParticipantID),
    FOREIGN KEY (FeedbackID) REFERENCES EventFeedback(FeedbackID)
);


-- Insert data into the User table
INSERT INTO User (UserID, Username, Password, Email, PhoneNo, FirstName, LastName, Role)
VALUES
(1, 'user1', 'password1', 'user1@email.com', '123-456-7890', 'John', 'Doe', 'Participant'),
(2, 'user2', 'password2', 'user2@email.com', '987-654-3210', 'Jane', 'Smith', 'Participant'),
(3, 'user3', 'password3', 'user3@email.com', '555-555-5555', 'Robert', 'Johnson', 'Event Planner'),
(4, 'user4', 'password4', 'user4@email.com', '111-222-3333', 'Alice', 'Williams', 'Participant'),
(5, 'user5', 'password5', 'user5@email.com', '999-888-7777', 'David', 'Brown', 'Event Planner'),
(6, 'user6', 'password6', 'user6@email.com', '444-777-8888', 'Emily', 'Davis', 'Participant'),
(7, 'user7', 'password7', 'user7@email.com', '333-999-1111', 'Michael', 'Miller', 'Event Planner'),
(8, 'user8', 'password8', 'user8@email.com', '222-111-4444', 'Sophia', 'Wilson', 'Participant'),
(9, 'user9', 'password9', 'user9@email.com', '777-333-5555', 'Ethan', 'Anderson', 'Participant'),
(10, 'user10', 'password10', 'user10@email.com', '666-666-6666', 'Olivia', 'Martinez', 'Administrator');

INSERT INTO User (UserID, Username, Password, Email, PhoneNo, FirstName, LastName, Role)
VALUES
(11, 'user11', 'password11', 'user11@email.com', '111-111-1111', 'William', 'Moore', 'Participant'),
(12, 'user12', 'password12', 'user12@email.com', '222-222-2222', 'Lily', 'Taylor', 'Participant'),
(13, 'user13', 'password13', 'user13@email.com', '333-333-3333', 'Daniel', 'Wilson', 'Event Planner'),
(14, 'user14', 'password14', 'user14@email.com', '444-444-4444', 'Ava', 'Jones', 'Participant'),
(15, 'user15', 'password15', 'user15@email.com', '555-555-5555', 'James', 'White', 'Event Planner'),
(16, 'user16', 'password16', 'user16@email.com', '666-666-6666', 'Grace', 'Johnson', 'Participant'),
(17, 'user17', 'password17', 'user17@email.com', '777-777-7777', 'Benjamin', 'Harris', 'Event Planner'),
(18, 'user18', 'password18', 'user18@email.com', '888-888-8888', 'Nora', 'Lewis', 'Participant'),
(19, 'user19', 'password19', 'user19@email.com', '999-999-9999', 'Samuel', 'Clark', 'Participant'),
(20, 'user20', 'password20', 'user20@email.com', '123-123-1234', 'Chloe', 'Turner', 'Administrator'),
(21, 'user21', 'password21', 'user21@email.com', '234-234-2345', 'Matthew', 'Baker', 'Participant'),
(22, 'user22', 'password22', 'user22@email.com', '345-345-3456', 'Sofia', 'Garcia', 'Participant'),
(23, 'user23', 'password23', 'user23@email.com', '456-456-4567', 'Elijah', 'Roberts', 'Event Planner'),
(24, 'user24', 'password24', 'user24@email.com', '567-567-5678', 'Liam', 'Martin', 'Participant'),
(25, 'user25', 'password25', 'user25@email.com', '678-678-6789', 'Aiden', 'Moore', 'Event Planner'),
(26, 'user26', 'password26', 'user26@email.com', '789-789-7890', 'Mia', 'Hall', 'Participant'),
(27, 'user27', 'password27', 'user27@email.com', '890-890-8901', 'Harper', 'Davis', 'Event Planner'),
(28, 'user28', 'password28', 'user28@email.com', '901-901-9012', 'Logan', 'Brown', 'Participant'),
(29, 'user29', 'password29', 'user29@email.com', '012-012-0123', 'Aiden', 'Smith', 'Participant'),
(30, 'user30', 'password30', 'user30@email.com', '321-321-3210', 'Ella', 'Anderson', 'Event Planner'),
(31, 'user31', 'password31', 'user31@email.com', '111-222-3333', 'Jackson', 'Johnson', 'Participant'),
(32, 'user32', 'password32', 'user32@email.com', '222-333-4444', 'Liam', 'Robinson', 'Participant'),
(33, 'user33', 'password33', 'user33@email.com', '333-444-5555', 'Grace', 'Smith', 'Event Planner'),
(34, 'user34', 'password34', 'user34@email.com', '444-555-6666', 'Lucas', 'Lee', 'Participant'),
(35, 'user35', 'password35', 'user35@email.com', '555-666-7777', 'Scarlett', 'Davis', 'Event Planner'),
(36, 'user36', 'password36', 'user36@email.com', '666-777-8888', 'Ethan', 'Carter', 'Participant'),
(37, 'user37', 'password37', 'user37@email.com', '777-888-9999', 'Luna', 'Miller', 'Event Planner'),
(38, 'user38', 'password38', 'user38@email.com', '888-999-0000', 'Oliver', 'Anderson', 'Participant'),
(39, 'user39', 'password39', 'user39@email.com', '999-000-1111', 'Emma', 'Parker', 'Participant'),
(40, 'user40', 'password40', 'user40@email.com', '123-456-7890', 'Noah', 'Harris', 'Event Planner');


-- Insert data into the Event table
INSERT INTO Event (EventID, EventName, EventDescription, EventDate, EventTime, Location, MaxCapacity, EventType, EventStatus)
VALUES
(1, 'Event 1', 'Description 1', '2023-11-10', '10:00:00', 'Location 1', 100, 'Type A', 'Active'),
(2, 'Event 2', 'Description 2', '2023-11-15', '15:30:00', 'Location 2', 150, 'Type B', 'Canceled'),
(3, 'Event 3', 'Description 3', '2023-11-20', '09:15:00', 'Location 3', 200, 'Type A', 'Active'),
(4, 'Event 4', 'Description 4', '2023-11-25', '14:00:00', 'Location 4', 120, 'Type C', 'Active'),
(5, 'Event 5', 'Description 5', '2023-11-30', '16:45:00', 'Location 5', 180, 'Type B', 'Completed'),
(6, 'Event 6', 'Description 6', '2023-12-05', '11:30:00', 'Location 6', 90, 'Type A', 'Active'),
(7, 'Event 7', 'Description 7', '2023-12-10', '19:00:00', 'Location 7', 130, 'Type B', 'Active'),
(8, 'Event 8', 'Description 8', '2023-12-15', '10:45:00', 'Location 8', 160, 'Type C', 'Active'),
(9, 'Event 9', 'Description 9', '2023-12-20', '13:15:00', 'Location 9', 110, 'Type A', 'Active'),
(10, 'Event 10', 'Description 10', '2023-12-25', '18:30:00', 'Location 10', 140, 'Type C', 'Active');

-- Insert data into the Participant table
INSERT INTO Participant (ParticipantID, UserID, DateOfBirth, PhoneNo, Address, PaymentInfo)
VALUES
(1, 1, '1990-01-15', '123-456-7890', 'Address 1', 'Payment Info 1'),
(2, 2, '1985-05-20', '987-654-3210', 'Address 2', 'Payment Info 2'),
(3, 3, '1980-11-03', '555-555-5555', 'Address 3', 'Payment Info 3'),
(4, 4, '1995-07-12', '111-222-3333', 'Address 4', 'Payment Info 4'),
(5, 5, '1993-02-28', '999-888-7777', 'Address 5', 'Payment Info 5'),
(6, 6, '1998-08-15', '444-777-8888', 'Address 6', 'Payment Info 6'),
(7, 7, '1992-06-10', '333-999-1111', 'Address 7', 'Payment Info 7'),
(8, 8, '1997-04-05', '222-111-4444', 'Address 8', 'Payment Info 8'),
(9, 9, '1991-09-30', '777-333-5555', 'Address 9', 'Payment Info 9'),
(10, 10, '1989-12-25', '666-666-6666', 'Address 10', 'Payment Info 10');

INSERT INTO Participant (ParticipantID, UserID, DateOfBirth, PhoneNo, Address, PaymentInfo)
VALUES
(11, 11, '1977-03-05', '111-111-1111', 'Address 11', 'Payment Info 11'),
(12, 12, '1983-09-15', '222-222-2222', 'Address 12', 'Payment Info 12'),
(13, 13, '1972-07-20', '333-333-3333', 'Address 13', 'Payment Info 13'),
(14, 14, '1990-05-02', '444-444-4444', 'Address 14', 'Payment Info 14'),
(15, 15, '1987-11-30', '555-555-5555', 'Address 15', 'Payment Info 15'),
(16, 16, '1995-08-10', '666-666-6666', 'Address 16', 'Payment Info 16'),
(17, 17, '1982-06-25', '777-777-7777', 'Address 17', 'Payment Info 17'),
(18, 18, '1989-04-20', '888-888-8888', 'Address 18', 'Payment Info 18'),
(19, 19, '1978-02-15', '999-999-9999', 'Address 19', 'Payment Info 19'),
(20, 20, '1981-01-10', '123-123-1234', 'Address 20', 'Payment Info 20'),
(21, 21, '1996-06-17', '234-234-2345', 'Address 21', 'Payment Info 21'),
(22, 22, '1984-10-02', '345-345-3456', 'Address 22', 'Payment Info 22'),
(23, 23, '1986-09-23', '456-456-4567', 'Address 23', 'Payment Info 23'),
(24, 24, '1975-03-08', '567-567-5678', 'Address 24', 'Payment Info 24'),
(25, 25, '1973-12-27', '678-678-6789', 'Address 25', 'Payment Info 25'),
(26, 26, '1988-07-14', '789-789-7890', 'Address 26', 'Payment Info 26'),
(27, 27, '1997-04-15', '890-890-8901', 'Address 27', 'Payment Info 27'),
(28, 28, '1983-08-12', '901-901-9012', 'Address 28', 'Payment Info 28'),
(29, 29, '1979-05-28', '012-012-0123', 'Address 29', 'Payment Info 29'),
(30, 30, '1980-11-04', '321-321-3210', 'Address 30', 'Payment Info 30'),
(31, 31, '1974-02-20', '111-222-3333', 'Address 31', 'Payment Info 31'),
(32, 32, '1982-10-15', '222-333-4444', 'Address 32', 'Payment Info 32'),
(33, 33, '1987-06-07', '333-444-5555', 'Address 33', 'Payment Info 33'),
(34, 34, '1976-09-29', '444-555-6666', 'Address 34', 'Payment Info 34'),
(35, 35, '1993-01-12', '555-666-7777', 'Address 35', 'Payment Info 35'),
(36, 36, '1981-04-01', '666-777-8888', 'Address 36', 'Payment Info 36'),
(37, 37, '1985-12-10', '777-888-9999', 'Address 37', 'Payment Info 37'),
(38, 38, '1992-08-18', '888-999-0000', 'Address 38', 'Payment Info 38'),
(39, 39, '1971-05-27', '999-000-1111', 'Address 39', 'Payment Info 39'),
(40, 40, '1988-03-22', '123-456-7890', 'Address 40', 'Payment Info 40');


-- Insert data into the EventFeedback table
INSERT INTO EventFeedback (FeedbackID, EventID, ParticipantID, Rating, Comments, FeedbackDate)
VALUES
(1, 1, 1, 4, 'Great event!', '2023-11-11'),
(2, 2, 2, 3, 'Good event, could be better.', '2023-11-16'),
(3, 3, 3, 5, 'Fantastic experience!', '2023-11-21'),
(4, 4, 4, 4, 'Enjoyed it a lot.', '2023-11-26'),
(5, 5, 5, 3, 'Not bad, but room for improvement.', '2023-12-01'),
(6, 6, 6, 5, 'Absolutely loved it!', '2023-12-06'),
(7, 7, 7, 4, 'Had a great time.', '2023-12-11'),
(8, 8, 8, 3, 'Good event overall.', '2023-12-16'),
(9, 9, 9, 5, 'Exceeded my expectations.', '2023-12-21'),
(10, 10, 10, 4, 'Well-organized and enjoyable.', '2023-12-26');

-- Insert data into the EventPlanner table
INSERT INTO EventPlanner (PlannerID, UserID, CompanyName, PhoneNo, EventsOrganized)
VALUES
(11, 9, 'Event Masters', '777-333-5555', '9, 10'),
(12, 3, 'Event Planning Co. 2', '555-555-5555', '1, 2, 3'),
(13, 5, 'Event Creators', '999-888-7777', '4, 5, 6'),
(14, 7, 'Event Pros', '333-999-1111', '7, 8, 9'),
(15, 8, 'Event Visionaries', '222-111-4444', '10'),
(16, 2, 'Event Magic', '987-654-3210', '1, 3, 5'),
(17, 4, 'Event Innovators', '111-222-3333', '2, 4, 6'),
(18, 6, 'Event Creations Inc.', '444-777-8888', '3, 5, 7'),
(19, 10, 'Event Planners United', '666-666-6666', '1, 4, 7'),
(20, 9, 'Event Gurus', '777-333-5555', '2, 5, 8');


-- Insert data into the Ticket table
INSERT INTO Ticket (TicketID, EventID, ParticipantID, TicketType, TicketPrice, PurchaseDate, PaymentStatus)
VALUES
(1, 1, 1, 'Regular', 50.00, '2023-11-12', 'Paid'),
(2, 2, 2, 'VIP', 100.00, '2023-11-17', 'Paid'),
(3, 3, 3, 'Regular', 55.00, '2023-11-22', 'Paid'),
(4, 4, 4, 'Regular', 45.00, '2023-11-27', 'Paid'),
(5, 5, 5, 'VIP', 110.00, '2023-12-02', 'Paid'),
(6, 6, 6, 'Regular', 60.00, '2023-12-07', 'Paid'),
(7, 7, 7, 'VIP', 120.00, '2023-12-12', 'Paid'),
(8, 8, 8, 'Regular', 65.00, '2023-12-17', 'Paid'),
(9, 9, 9, 'Regular', 48.00, '2023-12-22', 'Paid'),
(10, 10, 10, 'VIP', 130.00, '2023-12-27', 'Paid');

INSERT INTO Ticket (TicketID, EventID, ParticipantID, TicketType, TicketPrice, PurchaseDate, PaymentStatus)
VALUES
(11, 1, 11, 'Regular', 50.00, '2023-12-01', 'Paid'),
(12, 2, 12, 'VIP', 100.00, '2023-12-06', 'Paid'),
(13, 3, 13, 'Regular', 55.00, '2023-12-11', 'Paid'),
(14, 4, 14, 'Regular', 45.00, '2023-12-16', 'Paid'),
(15, 5, 15, 'VIP', 110.00, '2023-12-21', 'Paid'),
(16, 6, 16, 'Regular', 60.00, '2023-12-26', 'Paid'),
(17, 7, 17, 'VIP', 120.00, '2023-12-31', 'Paid'),
(18, 8, 18, 'Regular', 65.00, '2024-01-05', 'Paid'),
(19, 9, 19, 'Regular', 48.00, '2024-01-10', 'Paid'),
(20, 10, 20, 'VIP', 130.00, '2024-01-15', 'Paid'),
(21, 1, 21, 'Regular', 50.00, '2024-01-20', 'Paid'),
(22, 2, 22, 'VIP', 100.00, '2024-01-25', 'Paid'),
(23, 3, 23, 'Regular', 55.00, '2024-01-30', 'Paid'),
(24, 4, 24, 'Regular', 45.00, '2024-02-04', 'Paid'),
(25, 5, 25, 'VIP', 110.00, '2024-02-09', 'Paid'),
(26, 6, 26, 'Regular', 60.00, '2024-02-14', 'Paid'),
(27, 7, 27, 'VIP', 120.00, '2024-02-19', 'Paid'),
(28, 8, 28, 'Regular', 65.00, '2024-02-24', 'Paid'),
(29, 9, 29, 'Regular', 48.00, '2024-02-29', 'Paid'),
(30, 10, 30, 'VIP', 130.00, '2024-03-05', 'Paid'),
(31, 110, 31, 'Regular', 50.00, '2024-03-10', 'Paid'),
(32, 110, 32, 'VIP', 100.00, '2024-03-15', 'Paid'),
(33, 110, 33, 'Regular', 55.00, '2024-03-20', 'Paid'),
(34, 110, 34, 'Regular', 45.00, '2024-03-25', 'Paid'),
(35, 110, 35, 'VIP', 110.00, '2024-03-30', 'Paid'),
(36, 200, 36, 'Regular', 50.00, '2024-04-04', 'Paid'),
(37, 200, 37, 'VIP', 100.00, '2024-04-09', 'Paid'),
(38, 200, 38, 'Regular', 55.00, '2024-04-14', 'Paid'),
(39, 200, 39, 'Regular', 45.00, '2024-04-19', 'Paid'),
(40, 200, 40, 'VIP', 110.00, '2024-04-24', 'Paid');


-- Insert data into the AnalyticsData table
INSERT INTO AnalyticsData (AnalyticsID, EventID, AttendanceCount, Revenue, ReportDate)
VALUES
(1, 1, 80, 4000.00, '2023-11-13'),
(2, 2, 120, 12000.00, '2023-11-18'),
(3, 3, 150, 8250.00, '2023-11-23'),
(4, 4, 100, 4500.00, '2023-11-28'),
(5, 5, 160, 17600.00, '2023-12-03'),
(6, 6, 70, 4200.00, '2023-12-08'),
(7, 7, 110, 13200.00, '2023-12-13'),
(8, 8, 140, 9100.00, '2023-12-18'),
(9, 9, 90, 4320.00, '2023-12-23'),
(10, 10, 180, 23400.00, '2023-12-28');

-- Insert data into the Ticketing table
INSERT INTO Ticketing (TicketingID, EventID, ParticipantID, TicketID)
VALUES
(1, 1, 1, 1),
(2, 2, 2, 2),
(3, 3, 3, 3),
(4, 4, 4, 4),
(5, 5, 5, 5),
(6, 6, 6, 6),
(7, 7, 7, 7),
(8, 8, 8, 8),
(9, 9, 9, 9),
(10, 10, 10, 10);

-- Insert data into the Feedback table
INSERT INTO Feedback (FeedbackRelationshipID, EventID, ParticipantID, FeedbackID)
VALUES
(1, 1, 1, 1),
(2, 2, 2, 2),
(3, 3, 3, 3),
(4, 4, 4, 4),
(5, 5, 5, 5),
(6, 6, 6, 6),
(7, 7, 7, 7),
(8, 8, 8, 8),
(9, 9, 9, 9),
(10, 10, 10, 10);

DESCRIBE User;
DESCRIBE Event;
DESCRIBE Ticket;
DESCRIBE Participant;
DESCRIBE EventFeedback;
DESCRIBE EventPlanner;
DESCRIBE AnalyticsData;
DESCRIBE Ticketing;
DESCRIBE Feedback;

SELECT * FROM User;
SELECT * FROM Event;
SELECT * FROM Ticket;
SELECT * FROM Participant;
SELECT * FROM EventFeedback;
SELECT * FROM EventPlanner;
SELECT * FROM AnalyticsData;
SELECT * FROM Ticketing;
SELECT * FROM Feedback;

SELECT User, Host FROM mysql.user;

DELIMITER //

CREATE FUNCTION CalculateTotalRevenue(inputEventID INT) RETURNS DECIMAL(10, 2)
BEGIN
  DECLARE totalRevenue DECIMAL(10, 2);
  SELECT SUM(TicketPrice) INTO totalRevenue FROM Ticket WHERE EventID = inputEventID;
  RETURN totalRevenue;
END//

CREATE FUNCTION GetEventFeedbackAverageRating(inputEventID INT) RETURNS DECIMAL(3, 2)
BEGIN
  DECLARE avgRating DECIMAL(3, 2);
  SELECT AVG(Rating) INTO avgRating FROM EventFeedback WHERE EventID = inputEventID;
  RETURN avgRating;
END//

CREATE FUNCTION CountTicketsSold(inputEventID INT) RETURNS INT
BEGIN
  DECLARE soldTickets INT;
  SELECT COUNT(*) INTO soldTickets FROM Ticket WHERE EventID = inputEventID AND PaymentStatus = 'Paid';
  RETURN soldTickets;
END//

DELIMITER ;

DELIMITER //
CREATE PROCEDURE BookTicket(IN inputEventID INT, IN inputParticipantID INT, IN inputTicketType VARCHAR(255), IN inputTicketPrice DECIMAL(10,2), IN inputPaymentStatus VARCHAR(255))
BEGIN
    INSERT INTO Ticket (EventID, ParticipantID, TicketType, TicketPrice, PurchaseDate, PaymentStatus) 
    VALUES (inputEventID, inputParticipantID, inputTicketType, inputTicketPrice, NOW(), inputPaymentStatus);
END;

DELIMITER //
DROP TRIGGER IF EXISTS UpdateAttendanceCount;
CREATE TRIGGER UpdateAttendanceCount
AFTER INSERT ON Ticket
FOR EACH ROW
BEGIN
  DECLARE newEventID INT;CalculateTotalRevenue
  SET newEventID = NEW.EventID;
  UPDATE AnalyticsData SET AttendanceCount = AttendanceCount + 1 WHERE EventID = newEventID;
END//
DELIMITER ;

DELIMITER //
CREATE TRIGGER UpdateEventStatus
BEFORE INSERT ON Event
FOR EACH ROW
BEGIN
  IF NEW.EventDate < NOW() THEN
    SET NEW.EventStatus = 'Completed';
  ELSE
    SET NEW.EventStatus = 'Active';
  END IF;
END;
//
DELIMITER ;


DELIMITER ;

DROP FUNCTION IF EXISTS CalculateTotalRevenue;
DROP FUNCTION IF EXISTS GetEventFeedbackAverageRating;
DROP FUNCTION IF EXISTS CountTicketsSold;

SELECT CalculateTotalRevenue(2);
SELECT GetEventFeedbackAverageRating(2);
SELECT CountTicketsSold(2);		
























SET GLOBAL log_bin_trust_function_creators = 1;

-- Disable binary logging temporarily
SET SQL_LOG_BIN = 0;

-- Create your functions and triggers here

-- Re-enable binary logging
SET SQL_LOG_BIN = 1;

