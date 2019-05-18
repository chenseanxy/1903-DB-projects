use reservation;

create table flights(
	flightNum varchar(8) primary key,
    price int,
    numSeats int,
    numAvail int,
    fromCity varchar(120),
    arivCity varchar(120),
    param blob
);

create table hotels(
	hotelNum varchar(10) primary key,
    location varchar(120),
    price int,
    numRooms int,
    numAvail int,
	param blob
);

create table bus(
	busNum varchar(10) primary key,
    location varchar(120),
    price int,
    numSeats int,
    numAvail int,
    param blob
);

create table customers(
	custID int primary key,
    custName varchar(30)    
);

create table reservations(
	resvNum varchar(10) primary key,
    custID int references customers(custID),
    resvType int,
    resvKey varchar(10)
);
    