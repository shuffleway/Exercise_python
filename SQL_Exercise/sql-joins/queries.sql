-- first query
SELECT * FROM owners 
 FULL OUTER JOIN vehicles 
  ON owners.id = vehicles.owner_id;

-- second query
SELECT first_name, last_name, 
  COUNT(owner_id) FROM owners o 
  JOIN vehicles v on o.id=v.owner_id 
  GROUP BY (first_name, last_name) 
ORDER BY first_name;

--Third query
SELECT first_name, last_name, 
  ROUND(AVG(price)) as average_price, COUNT(owner_id) FROM owners
  JOIN vehicles ON owners.id = vehicles.owner_id
  GROUP BY (first_name, last_name)
  HAVING COUNT(owner_id) > 1 AND ROUND(AVG(price)) > 10000
ORDER BY first_name DESC;
