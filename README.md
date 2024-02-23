# purchase
#Havi vssárlások követése

##adatbázisban tárolt mezők
ID PRYMARY KEY AUTOINCREMENT
month
day
shop
cost
comment

##a form elemei

hónap select > 12 hónap rögzítve
nap select > ha változik a hónap változik a napok száma is 
bolt datalist > keresse ki az adatbázisból a boltokat
költség input text > regexel tesztelve
megjegyzés input text > nem kötelező

## form működése
a hónapot, napot, boltot mindíg jegyezze meg
(Localstorage használata)
(<option value="" selected disable hidden>Choose here</option>)

a form küldésekor mindíg ellenőrizze az adatokat
(onsubmit="return validate()"

##sqlite

SELECT * FROM koltsegek ordered by month, day;
INSERT INTO koltsegek (month, day, shop, cost, comment) VALUES (?,?,?,?,?);
UPDATE koltsegek
SET month=?, day=?, shop=?, cost=?, cost=?, comment=? WHERE ID=?;
DELETE FROM koltsegek WHERE ID=?;

Költés boltonként összesen:
SELECT shop, sum(cost) FROM spend GROUP BY shop;
Költés boltonként havonta:
SELECT shop, sum(cost) FROM spend WHERE month=? GROUP BY shop;
select shop as 'Bolt',
count(shop) as 'Vásárlások száma',
sum(cost) as 'Költés' from spend
where month=1
group by shop
order by "Vásárlások száma";
