-- Volem executar una sèrie de consultes a una base de dades que serveix per gestionar les compres online d'un dels supermercats més importants de Catalunya. A l'arxiu adjunt número 1 trobaràs l'script de creació d'aquesta base de dades i a l'arxiu adjunt número 2 es mostra el seu esquema.
-- IMPORTANT: a l'arxiu adjunt número 3 es mostra el resultat que s'ha d'obtenir al executar cadascuna de les consultes.


-- 1. Fes una consulta que mostri la quantitat de paraules que contenen eñes castellanes (caràcter ñ) i eñes catalanes (caràcters ny) existents a la base de dades entre noms de províncies, noms de poblacions, noms de clients, cognoms de clients, noms de productes i noms de categories.

  select sum(num) as numero
  from
  (select COUNT(id_provincia) as num from provincies where nom like'%ñ%' or nom like '%ny%'
	union
	select COUNT(id_poblacio) as num from poblacions where nom like'%ñ%' or nom like '%ny%'
	union
	select COUNT(id_client) as num from clients where nom like'%ñ%' or nom like '%ny%'
	union
	select COUNT(codi) as num from productes where nom like'%ñ%' or nom like '%ny%'
	union
	select COUNT(id_categoria) as num from categorias where nom like'%ñ%' or nom like '%ny%'

)as anyos;
-- 2. Fes una consulta que mostri aquelles poblacions que estan emmagatzemades a la base de dades però a les quals no hi resideix cap client. Mostra els resultats ordenats pel nom de les poblacions.
-- IMPORTANT: aquesta consulta s'ha de realitzar amb subconsultes. És a dir, no es poden fer servir les clàusules LEFT JOIN o RIGHT JOIN.

 SELECT DISTINCT poblacions.nom
 from	poblacions
 left join clients on poblacions.id_poblacio = clients.poblacio
where clients.poblacio is null
order by poblacions.nom;

select pb.nom
from poblacions pb
where pb.id_poblacio not in (
	select distinct cl.poblacio
	from clients cl
)
order by pb.nom;

-- 3. Fes una consulta que mostri el nom, els cognoms, el telèfon i l'email d'aquells clients que estan emmagatzemats a la base de dades però encara no han realitzat cap compra. Mostra els resultats ordenats pel nom de les poblacions.
-- IMPORTANT: aquesta consulta s'ha de realitzar amb subconsultes. És a dir, no es poden fer servir les clàusules LEFT JOIN o RIGHT JOIN.

 SELECT * FROM clients;
 select * from comandes;
 select distinct client from comandes;
 
 select cl.nom, cl.cognoms, cl.telefon, cl.email
 from clients.cl
 inner join poblacions pb on pb.id_poblacion=cl.poblacio
 where cl.id_client not in (select distinct scm.client
	from comandes scm)
    order by pb.nom;

-- 4. Fes una consulta que mostri el nom d'aquells productes que tenen mes unitats en stock que el promig d'unitats en stock. Mostra els resultats ordenats pel nom dels productes.


 select pr.nom
 from productes pr
 where pr.unitats_stock > (select avg(spr.unitats_stock)
	from productes spr);

-- 5. Fes una consulta que mostri el nom d'aquells productes que tenen un preu inferior al preu mig de la categoria a la que pertanyen. Mostra el resultats ordenats pel nom del productes.

select pr.nom
from productes pr
where pr.preu < (
	select avg(sub_pr.preu)
	from productes sub_pr
    where sub_pr.categoria = pr.categoria
    );
-- 6. Fes una consulta que mostri el NIF, el nom i els cognoms dels 10 clients mes rentables. Calculem la rentabilitat d'un client dividint el total d'euros que ha gastat entre el total de compres que ha realitzat (euros gastats / compres realitzades).

 SELECT
  cl.nif,
  cl.nom,
  cl.cognoms,
  (SUM(dc.quantitat * pr.preu) / COUNT(DISTINCT co.numero)) AS rentabilitat
FROM clients cl
JOIN comandes co        ON co.client = cl.idclient
JOIN detallcomandes dc  ON dc.comanda = co.numero
JOIN productes pr       ON pr.codi = dc.producte
GROUP BY cl.idclient, cl.nif, cl.nom, cl.cognoms
ORDER BY rentabilitat DESC
LIMIT 10;


-- 7. Fes una consulta que mostri la quantitat d'ampolles de whisky, juntament amb la quantitat d'ampolles d'aigua, comprades a cadascuna de les províncies (es a dir, productes que contenen al nom la paraula whisky i productes que contenen al nom les paraules agua o aigua). Mostra els resultats ordenats pel nom de la província.

 SELECT
  pv.nom AS provincia,
  SUM(CASE WHEN LOWER(pr.nom) LIKE '%whisky%' THEN dc.quantitat ELSE 0 END) AS ampolles_whisky,
  SUM(CASE WHEN LOWER(pr.nom) LIKE '%agua%' OR LOWER(pr.nom) LIKE '%aigua%'
           THEN dc.quantitat ELSE 0 END) AS ampolles_aigua
FROM provincies pv
JOIN poblacions pb      ON pb.provincia = pv.idprovincia
JOIN clients cl         ON cl.poblacio = pb.idpoblacio
JOIN comandes co        ON co.client = cl.idclient
JOIN detallcomandes dc  ON dc.comanda = co.numero
JOIN productes pr       ON pr.codi = dc.producte
GROUP BY pv.idprovincia, pv.nom
ORDER BY pv.nom;


-- 8. Fes una consulta que mostri el NIF dels clients de les províncies de Girona, Lleida o Tarragona que han realitzat més comandes que algun client de la província de Barcelona.

 SELECT DISTINCT cl.nif
FROM clients cl
JOIN poblacions pb ON pb.idpoblacio = cl.poblacio
JOIN provincies pv ON pv.idprovincia = pb.provincia
WHERE pv.nom IN ('Girona', 'Lleida', 'Tarragona')
  AND (
    SELECT COUNT(*)
    FROM comandes co
    WHERE co.client = cl.idclient
  ) > ANY (
    SELECT
      (SELECT COUNT(*) FROM comandes co2 WHERE co2.client = clb.idclient)
    FROM clients clb
    JOIN poblacions pbb ON pbb.idpoblacio = clb.poblacio
    JOIN provincies pvb ON pvb.idprovincia = pbb.provincia
    WHERE pvb.nom = 'Barcelona'
  );


-- 9. Fes una consulta que mostri, per cadascuna de les províncies, la població que més benefici ha donat al supermercat (es a dir, on més diners s'han gastat). Mostra els resultats ordenats pel nom de la població.

 SELECT
  pv.nom AS provincia,
  pb.nom AS poblacio,
  SUM(dc.quantitat * pr.preu) AS benefici
FROM provincies pv
JOIN poblacions pb     ON pb.provincia = pv.idprovincia
JOIN clients cl        ON cl.poblacio = pb.idpoblacio
JOIN comandes co       ON co.client = cl.idclient
JOIN detallcomandes dc ON dc.comanda = co.numero
JOIN productes pr      ON pr.codi = dc.producte
GROUP BY pv.idprovincia, pv.nom, pb.idpoblacio, pb.nom
HAVING SUM(dc.quantitat * pr.preu) >= ALL (
  SELECT SUM(dc2.quantitat * pr2.preu)
  FROM poblacions pb2
  JOIN clients cl2        ON cl2.poblacio = pb2.idpoblacio
  JOIN comandes co2       ON co2.client = cl2.idclient
  JOIN detallcomandes dc2 ON dc2.comanda = co2.numero
  JOIN productes pr2      ON pr2.codi = dc2.producte
  WHERE pb2.provincia = pv.idprovincia
  GROUP BY pb2.idpoblacio
)
ORDER BY pb.nom;


-- 10. Fes una consulta que mostri els municipis de la província de Barcelona que han donat més benefici al supermercat que qualsevol de les ciutats importants de la província (Barcelona, L'Hospitalet de Llobregat, Sabadell, Terrassa, Santa Coloma de Gramanet i Mataró). Mostra els resultats ordenats pel nom de la població.

 SELECT
  pb.nom AS poblacio,
  SUM(dc.quantitat * pr.preu) AS benefici
FROM provincies pv
JOIN poblacions pb     ON pb.provincia = pv.idprovincia
JOIN clients cl        ON cl.poblacio = pb.idpoblacio
JOIN comandes co       ON co.client = cl.idclient
JOIN detallcomandes dc ON dc.comanda = co.numero
JOIN productes pr      ON pr.codi = dc.producte
WHERE pv.nom = 'Barcelona'
GROUP BY pb.idpoblacio, pb.nom
HAVING SUM(dc.quantitat * pr.preu) > ALL (
  SELECT SUM(dc2.quantitat * pr2.preu)
  FROM provincies pv2
  JOIN poblacions pb2     ON pb2.provincia = pv2.idprovincia
  JOIN clients cl2        ON cl2.poblacio = pb2.idpoblacio
  JOIN comandes co2       ON co2.client = cl2.idclient
  JOIN detallcomandes dc2 ON dc2.comanda = co2.numero
  JOIN productes pr2      ON pr2.codi = dc2.producte
  WHERE pv2.nom = 'Barcelona'
    AND pb2.nom IN ('Barcelona',
                    'L''Hospitalet de Llobregat',
                    'Sabadell',
                    'Terrassa',
                    'Santa Coloma de Gramanet',
                    'Mataró')
  GROUP BY pb2.idpoblacio, pb2.nom
)
ORDER BY pb.nom;

-- 11. Fes una consulta que mostri, per cadascuna de les categories dels productes, els cognoms i el nom del client (o clients, en cas d'empat) que ha adquirit més quantitat de productes d'aquella categoria.

 SELECT
  ca.nom AS categoria,
  cl.cognoms,
  cl.nom,
  SUM(dc.quantitat) AS total_unitats
FROM categories ca
JOIN productes pr      ON pr.categoria = ca.idcategoria
JOIN detallcomandes dc ON dc.producte = pr.codi
JOIN comandes co       ON co.numero = dc.comanda
JOIN clients cl        ON cl.idclient = co.client
GROUP BY ca.idcategoria, ca.nom, cl.idclient, cl.cognoms, cl.nom
HAVING SUM(dc.quantitat) >= ALL (
  SELECT SUM(dc2.quantitat)
  FROM productes pr2
  JOIN detallcomandes dc2 ON dc2.producte = pr2.codi
  JOIN comandes co2       ON co2.numero = dc2.comanda
  WHERE pr2.categoria = ca.idcategoria
  GROUP BY co2.client
)
ORDER BY ca.nom, cl.cognoms, cl.nom;

-- 12. Fes una consulta que mostri el nom del producte (o productes, en cas d'empat) més venut a cadascuna de les províncies.

 SELECT
  pv.nom AS provincia,
  pr.nom AS producte,
  SUM(dc.quantitat) AS unitats
FROM provincies pv
JOIN poblacions pb     ON pb.provincia = pv.idprovincia
JOIN clients cl        ON cl.poblacio = pb.idpoblacio
JOIN comandes co       ON co.client = cl.idclient
JOIN detallcomandes dc ON dc.comanda = co.numero
JOIN productes pr      ON pr.codi = dc.producte
GROUP BY pv.idprovincia, pv.nom, pr.codi, pr.nom
HAVING SUM(dc.quantitat) >= ALL (
  SELECT SUM(dc2.quantitat)
  FROM poblacions pb2
  JOIN clients cl2        ON cl2.poblacio = pb2.idpoblacio
  JOIN comandes co2       ON co2.client = cl2.idclient
  JOIN detallcomandes dc2 ON dc2.comanda = co2.numero
  WHERE pb2.provincia = pv.idprovincia
  GROUP BY dc2.producte
)
ORDER BY pv.nom, pr.nom;

-- 13. Fes una consulta que elimini de la base de dades aquelles poblacions on no hi resideix cap client.

 DELETE FROM poblacions
WHERE idpoblacio NOT IN (
  SELECT DISTINCT poblacio
  FROM clients
);

-- 14. Fes una consulta que incrementi un 10% el preu dels 15 productes més venuts.

 UPDATE productes
SET preu = preu * 1.10
WHERE codi IN (
  SELECT producte
  FROM (
    SELECT dc.producte
    FROM detallcomandes dc
    GROUP BY dc.producte
    ORDER BY SUM(dc.quantitat) DESC
    LIMIT 15
  ) t
);

-- 15. Fes una consulta que mostri el NIF, el nom i els cognoms d'aquells clients que tenen un codi postal que acaba en 3 i resideixen a una població on hi resideix un client que ha comprat alguna vegada Oli verge extra Carbonell 1 l.
-- IMPORTANT: aquesta consulta s'ha de resoldre utilitzant la clàusula EXISTS.

SELECT cl.nif, cl.nom, cl.cognoms
FROM clients cl
WHERE cl.codipostal LIKE '%3'
  AND EXISTS (
    SELECT 1
    FROM clients cl2
    JOIN comandes co       ON co.client = cl2.idclient
    JOIN detallcomandes dc ON dc.comanda = co.numero
    WHERE cl2.poblacio = cl.poblacio
      AND dc.producte = 'OLI00014'
  );