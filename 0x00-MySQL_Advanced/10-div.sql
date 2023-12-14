-- script that creates a function that divides the first by the
-- second number or returns 0 if the second number is equal to 0

DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
	DECLARE result FLOAT;

	IF b <> 0 THEN
		SET result = a / b;
	ELSE
		SET result = 0;
	END IF;

	RETURN result;
END $$

DELIMITER ;

