-- SQL script that creates a stored procedure

DELIMITER //

CREATE PROCEDURE AddBonus(
    IN in_user_id INT,
    IN in_project_name VARCHAR(255),
    IN in_score INT
)
BEGIN
    DECLARE project_exists INT;

    -- Check if the project already exists
    SELECT COUNT(*) INTO project_exists
    FROM projects
    WHERE name = in_project_name;

    IF project_exists = 0 THEN
        -- Project doesn't exist, create it
        INSERT INTO projects (name) VALUES (in_project_name);
    END IF;

    -- Add correction
    INSERT INTO corrections (user_id, project_id, score)
    SELECT in_user_id, id, in_score
    FROM projects
    WHERE name = in_project_name;
END //

DELIMITER ;

