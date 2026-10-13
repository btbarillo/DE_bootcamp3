SELECT 
    e.id AS earthquake_id,
    e.place,
    e.magnitude,
    e.event_time,
    c.country_name,
    c.region,
    c.risk_threshold_mag,
    c.emergency_contact_email,
    CASE 
        WHEN e.magnitude >= c.risk_threshold_mag THEN 'CRITICAL ALERT'
        ELSE 'MONITOR'
    END AS alert_status
FROM `berns_earthquake_db.table_earthquakes` e
LEFT JOIN (
    SELECT DISTINCT 
        country_name, 
        region, 
        emergency_contact_email, 
        risk_threshold_mag
    FROM `berns_earthquake_db.table_users_countries`
) c
    ON REGEXP_CONTAINS(LOWER(e.place), CONCAT(r'\b', LOWER(c.country_name), r'\b'))
WHERE e.magnitude >= 4.0 
    AND DATE(e.event_time) = '2026-10-07'  /* #CURRENT_DATE() OR 2026-MM-DD */
ORDER BY e.magnitude DESC;