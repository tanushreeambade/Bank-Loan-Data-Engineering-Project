-- 1. Total Records
SELECT COUNT(*) AS total_records
FROM bank_loan_data;

-- 2. Loan Approval Status
SELECT loan_status, COUNT(*) AS total
FROM bank_loan_data
GROUP BY loan_status;

-- 3. Gender-wise Loan Applications
SELECT gender, COUNT(*) AS total
FROM bank_loan_data
GROUP BY gender;

-- 4. Education-wise Applicants
SELECT education, COUNT(*) AS total
FROM bank_loan_data
GROUP BY education;

-- 5. Property Area Distribution
SELECT property_area, COUNT(*) AS total
FROM bank_loan_data
GROUP BY property_area;

-- 6. Income Category Distribution
SELECT income_category, COUNT(*) AS total
FROM bank_loan_data
GROUP BY income_category;

-- 7. Loan Category Distribution
SELECT loan_category, COUNT(*) AS total
FROM bank_loan_data
GROUP BY loan_category;

SELECT
ROUND(
100.0 * SUM(CASE WHEN loan_status='Y' THEN 1 ELSE 0 END)
/ COUNT(*),
2
) AS approval_rate;

SELECT
ROUND(AVG(loan_amount),2) AS avg_loan_amount
FROM bank_loan_data;

SELECT
education,
ROUND(AVG(total_income),2) AS avg_income
FROM bank_loan_data
GROUP BY education;

SELECT
education,
loan_status,
COUNT(*) AS total
FROM bank_loan_data
GROUP BY education, loan_status
ORDER BY education;

SELECT
property_area,
loan_status,
COUNT(*) AS total
FROM bank_loan_data
GROUP BY property_area, loan_status;

SELECT
loan_status,
ROUND(AVG(total_income),2) AS avg_income
FROM bank_loan_data
GROUP BY loan_status;

SELECT
credit_history,
loan_status,
COUNT(*) AS total
FROM bank_loan_data
GROUP BY credit_history, loan_status
ORDER BY credit_history;

SELECT
self_employed,
loan_status,
COUNT(*) AS total
FROM bank_loan_data
GROUP BY self_employed, loan_status;

SELECT
income_category,
loan_status,
COUNT(*) AS total
FROM bank_loan_data
GROUP BY income_category, loan_status;

SELECT
property_area,
ROUND(AVG(loan_amount),2) AS avg_loan
FROM bank_loan_data
GROUP BY property_area;


