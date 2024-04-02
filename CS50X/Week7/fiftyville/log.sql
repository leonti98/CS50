-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Identify crime of stolen duck crime with given date and street.
SELECT *
FROM crime_scene_reports
WHERE month = 7 AND day = 28
AND street = 'Humphrey Street';
-- id = 296
-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time
-- – each of their interview transcripts mentions the bakery.

-- search information from bakery in logs
SELECT hour, minute, activity, license_plate
FROM bakery_security_logs
WHERE month = 7 AND day = 28
AND hour BETWEEN 10 AND 11;

-- identify cars which left after crime
-- | 10   | 16     | exit     | 5P2BI95       |
-- | 10   | 18     | exit     | 94KL13X       |
-- | 10   | 18     | exit     | 6P58WS2       |
-- | 10   | 19     | exit     | 4328GD8

-- get more information from interviews
SELECT transcript FROM interviews WHERE day = 28 AND month = 7;
-- | Sometime within ten minutes of the theft, I saw the thief get into a car in
-- the bakery parking lot and drive away. If you have security footage from the
-- bakery parking lot,
--  you might want to look for cars that left the parking lot in that time frame.
                                                     |
-- | I don't know the thief's name, but it was someone I recognized. Earlier this morning,
-- before I arrived at Emma's bakery, I was walking by the ATM on
-- Leggett Street and saw the thief there withdrawing some money.
                                                                                         |
-- | As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
-- In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville
-- tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |

-- get correct infromation from bakery logs
SELECT hour, minute, activity, license_plate
FROM bakery_security_logs
WHERE month = 7 AND day = 28
AND hour BETWEEN 10 AND 11
AND minute BETWEEN 15 and 25;
-- +------+--------+----------+---------------+
-- | hour | minute | activity | license_plate |
-- +------+--------+----------+---------------+
-- | 10   | 16     | exit     | 5P2BI95       |
-- | 10   | 18     | exit     | 94KL13X       |
-- | 10   | 18     | exit     | 6P58WS2       |
-- | 10   | 19     | exit     | 4328GD8       |
-- | 10   | 20     | exit     | G412CB7       |
-- | 10   | 21     | exit     | L93JTIZ       |
-- | 10   | 23     | exit     | 322W7JE       |
-- | 10   | 23     | exit     | 0NTHK55       |
-- +------+--------+----------+---------------+

-- check withdrawals from ATM at Leggett Street
SELECT account_number, transaction_type, amount
FROM atm_transactions
WHERE month = 7 AND day = 28
AND transaction_type = 'withdraw'
AND atm_location = 'Leggett Street';
-- +----------------+------------------+--------+
-- | account_number | transaction_type | amount |
-- +----------------+------------------+--------+
-- | 28500762       | withdraw         | 48     |
-- | 28296815       | withdraw         | 20     |
-- | 76054385       | withdraw         | 60     |
-- | 49610011       | withdraw         | 50     |
-- | 16153065       | withdraw         | 80     |
-- | 25506511       | withdraw         | 20     |
-- | 81061156       | withdraw         | 30     |
-- | 26013199       | withdraw         | 35     |
-- +----------------+------------------+--------+

-- get more infromation from phone calls
SELECT caller, receiver, duration
FROM phone_calls
WHERE month = 7 AND day = 28
AND year = 2023;

-- combine phone call, license plate AND ATM transaction information, to narrow suspect list
SELECT id, name, passport_number FROM people
WHERE id IN (
    SELECT person_id
    FROM bank_accounts
    WHERE account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE month = 7 AND day = 28
        AND transaction_type = 'withdraw'
        AND atm_location = 'Leggett Street'
    )
)
AND license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE month = 7 AND day = 28
    AND hour BETWEEN 10 AND 11
    AND minute BETWEEN 15 and 25
)
AND phone_number IN (
    SELECT caller
    FROM phone_calls
    WHERE month = 7 AND day = 28
    AND year = 2023
);
-- we are left with two suspects
-- +--------+-------+-----------------+
-- |   id   | name  | passport_number |
-- +--------+-------+-----------------+
-- | 514354 | Diana | 3592750733      |
-- | 686048 | Bruce | 5773159633      |
-- +--------+-------+-----------------+

-- check city naming in airports table
SELECT * FROM airports LIMIT 10;

--get Fiftyville airport id
SELECT id
FROM airports
WHERE city = 'Fiftyville';
-- 8

-- get flight id
SELECT id, hour FROM flights
WHERE origin_airport_id = 8
AND year = 2023
AND month = 7 AND day = 28;
-- +----+
-- | id |
-- +----+
-- | 1  |
-- | 6  |
-- | 17 |
-- | 34 |
-- | 35 |
-- +----+

SELECT * FROM passengers
WHERE flight_id IN (
    SELECT id FROM flights
    WHERE origin_airport_id = 8
    AND year = 2023
    AND month = 7 AND day = 28
)
AND passport_number = 3592750733
OR passport_number = 5773159633;
-- +-----------+-----------------+------+
-- | flight_id | passport_number | seat |
-- +-----------+-----------------+------+
-- | 36        | 5773159633      | 4A   |
-- +-----------+-----------------+------+

-- We have only one suspect left
SELECT * FROM people
WHERE passport_number = 5773159633;
-- +--------+-------+----------------+-----------------+---------------+
-- |   id   | name  |  phone_number  | passport_number | license_plate |
-- +--------+-------+----------------+-----------------+---------------+
-- | 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
-- +--------+-------+----------------+-----------------+---------------+

-- check phone calls from Bruse on crime day
SELECT receiver, duration FROM phone_calls
WHERE month = 7 AND day = 28
AND year = 2023 AND caller = '(367) 555-5533';
-- +----------------+----------+
-- |    receiver    | duration |
-- +----------------+----------+
-- | (375) 555-8161 | 45       |
-- | (344) 555-9601 | 120      |
-- | (022) 555-4052 | 241      |
-- | (704) 555-5790 | 75       |
-- +----------------+----------+

-- Get destination of flight with id 32
SELECT city FROM airports WHERE id = (
    SELECT destination_airport_id FROM flights WHERE id = 36
);
-- +---------------+
-- |     city      |
-- +---------------+
-- | New York City |
-- +---------------+

-- only call to person with number (375) 555-8161 is less than a minute
SELECT * FROM people WHERE phone_number = '(375) 555-8161';
-- +--------+-------+----------------+-----------------+---------------+
-- |   id   | name  |  phone_number  | passport_number | license_plate |
-- +--------+-------+----------------+-----------------+---------------+
-- | 864400 | Robin | (375) 555-8161 | NULL            | 4V16VO0       |
-- +--------+-------+----------------+-----------------+---------------+
