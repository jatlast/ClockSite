/* Create Stored Procedure - spCustomerSearch() */
DELIMITER //

CREATE OR REPLACE PROCEDURE
    spCustomerSearch(pName varchar(32), pPhone char(10))
    BEGIN
        SELECT cName, cPhone FROM Customer
        Where (
                CHAR_LENGTH(pName) > 3
                AND
                LOWER(cName) LIKE CONCAT('%', LOWER(pName), '%')
        )
        OR (
            CHAR_LENGTH(pPhone) > 2
	    AND
            cPhone LIKE CONCAT('%', pPhone, '%')
        );
    END;

//

DELIMITER ;

CALL spCustomerSearch('M', '7');
