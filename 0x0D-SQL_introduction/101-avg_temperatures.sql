--  displays the average temperature (Fahrenheit) by city ordered by temperature

Select city, AVG(value) AS avg_temp from temperatures GROUP by city ORDER BY avg_temp DESC;
