/*##############################################################
# Consultas SQL varias
# Autor: Diana Chacón Ocariz
############################################################### */

/* EJERCICIO 1 */
/* Id de los clientes */
SELECT id FROM Clients

/* EJERCICIO 2 */
/* Id de los clientes ordenados por RUT */
SELECT id 
FROM Clients
ORDER BY taxNumber

/* EJERCICIO 3 */
/* Clientes con su saldo total, ordenados por saldo decreciente */
SELECT cl.id, cl.name, sum(ac.balance)
FROM Clients cl JOIN Accounts ac ON cl.id = ac.clientId
GROUP BY cl.id 
ORDER BY sum(ac.balance) DESC

/* EJERCICIO 4 */
/* Bancos con sus clientes y sus RUT ordenados por */
/* nombre del banco y nombre de los clientes */
SELECT DISTINCT bk.name, cl.name, cl.taxNumber
FROM Banks bk JOIN Accounts ac ON bk.id = ac.bankId 
JOIN Clients cl ON cl.id = ac.clientId
ORDER BY bk.name, cl.name

/* EJERCICIO 5 */
/* Clientes del banco Santander con un saldo mayor a 25000 */
/* ordenados por saldo decreciente */
SELECT cl.id, cl.name, sum(ac.balance)
FROM Clients cl JOIN Accounts ac ON cl.id = ac.clientId
WHERE ac.bankId = 1
GROUP BY cl.id 
HAVING sum(ac.balance) >= 25000
ORDER BY sum(ac.balance) DESC

/* EJERCICIO 6 */
/* Bancos con el total de dinero que manejan */
/* ordenados crecientemente */
SELECT DISTINCT bk.id, bk.name, sum(ac.balance)
FROM Banks bk JOIN Accounts ac ON bk.id = ac.bankId
GROUP BY bk.id, bk.name
ORDER BY sum(ac.balance) 

/* EJERCICIO 7 */
/* Bancos con la cantidad de clientes que solo están en ese banco */
/* Solo los clientes id = 4 y 6 tienen cuenta en un solo banco */
SELECT ac.bankId, count(DISTINCT ac.clientId)
FROM Accounts ac
WHERE ac.clientId NOT IN (SELECT ac2.clientId FROM Accounts ac2 WHERE ac.bankId <> ac2.bankId)
GROUP BY ac.bankId

SELECT ac.bankId, ac.clientId
FROM Accounts ac
WHERE ac.clientId NOT IN (SELECT ac2.clientId FROM Accounts ac2 WHERE ac.bankId <> ac2.bankId)
GROUP BY ac.bankId


/* EJERCICIO 8 */
/* Bancos con el cliente de menor saldo */

/* Vista con los bancos, sus clientes y el saldo total de cada uno */
CREATE VIEW TotalBalanceBankClient AS
SELECT ac.bankId AS bankId, ac.clientId AS clientId, sum(ac.balance) AS total
FROM Accounts ac
GROUP BY ac.bankId, ac.clientId

/* Bancos con el nombre del cliente con el menor saldo */
SELECT bk.name, cl.name, min(tb.total)
FROM Banks bk JOIN TotalBalanceBankClient tb ON bk.id = tb.bankId 
JOIN Clients cl ON tb.clientId = cl.id
GROUP BY tb.bankId 
