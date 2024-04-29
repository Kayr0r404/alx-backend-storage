-- Drop the trigger if it exists
DROP TRIGGER IF EXISTS resets_valid_email;

-- Change delimiter to define trigger body
DELIMITER $$

-- Create the trigger
CREATE TRIGGER resets_valid_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email has been changed
    IF OLD.email <> NEW.email THEN
        -- Reset the valid_email attribute to 0 for the updated email
        UPDATE users
        SET valid_email = 0
        WHERE email = NEW.email;
    else
        set valid_email = OLD.valid_email
        where email = new.email
    END IF;
END $$

-- Reset delimiter to default
DELIMITER ;
