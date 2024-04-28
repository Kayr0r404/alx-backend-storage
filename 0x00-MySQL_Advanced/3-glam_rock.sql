-- Query to list Glam rock bands ranked by longevity
SELECT band_name, (2022 - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
