DELETE FROM authtoken_token WHERE user_id=2;
DELETE FROM authtoken_token WHERE user_id=3;
DELETE FROM auth_user WHERE id=4;
DELETE FROM app_api_favorite WHERE id=3;
DROP TABLE app_api_myopsuser

SELECT c.*, j.*
FROM app_api_checkin c 
JOIN app_api_journal j 
    ON c.date=j.date
