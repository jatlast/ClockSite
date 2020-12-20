
CREATE OR REPLACE VIEW WorkOrderDurations AS
SELECT CASE
        WHEN woDateFinished IS NOT NULL
            THEN(CONCAT('Clock was finished '
                        , TIMESTAMPDIFF(YEAR,woDateFinished,NOW()), ' years, '
                        , MOD(TIMESTAMPDIFF(MONTH,woDateFinished,NOW()),12), ' months, '
                        , MOD(TIMESTAMPDIFF(DAY,woDateFinished,NOW()),30), ' days ago')
                )
        WHEN woDateFinished IS NULL 
            AND woDateStarted IS NOT NULL
            THEN(CONCAT('Clock took '
                        , TIMESTAMPDIFF(YEAR,woDate,woDateStarted), ' years, '
                        , MOD(TIMESTAMPDIFF(MONTH,woDate,woDateStarted),12), ' months, '
                        , MOD(TIMESTAMPDIFF(DAY,woDate,woDateStarted),30), ' days to complete')
                )
        WHEN woDateFinished IS NULL 
            AND woDateStarted IS NULL
            THEN (CONCAT('Clock has been in queue for '
                        , TIMESTAMPDIFF(YEAR,woDate,NOW()), ' years, '
                        , MOD(TIMESTAMPDIFF(MONTH,woDate,NOW()),12), ' months, '
                        , MOD(TIMESTAMPDIFF(DAY,woDate,NOW()),30), ' days')
                )
            ELSE 'Duration Unknown'
        END as durationQ
    , CASE
        WHEN woDateStarted IS NOT NULL
            AND woDateFinished IS NOT NULL
            THEN(CONCAT('Clock took '
                        , TIMESTAMPDIFF(YEAR,woDateStarted,woDateFinished), ' years, '
                        , MOD(TIMESTAMPDIFF(MONTH,woDateStarted,woDateFinished),12), ' months, '
                        , MOD(TIMESTAMPDIFF(DAY,woDateStarted,woDateFinished),30), ' days to complete')
                )
        WHEN woDateFinished IS NULL 
            AND woDateStarted IS NULL
            THEN 'In Queue'
            ELSE 'Same Day Service'
        END as DurationToFinish
    , (CONCAT('Clock was brought in '
                , TIMESTAMPDIFF(YEAR,woDate,NOW()), ' years, '
                , MOD(TIMESTAMPDIFF(MONTH,woDate,NOW()),12), ' months, '
                , MOD(TIMESTAMPDIFF(DAY,woDate,NOW()),30), ' days ago')
        )  as DurationSinceDropOff
    , WorkOrders.*
from WorkOrders;



