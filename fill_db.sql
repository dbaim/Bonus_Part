INSERT INTO DiseaseType (id, description) VALUES
(1, 'molecular disease'),
(2, 'virology'),
(3, 'cell disease'),
(4, 'tissue disease'),
(5, 'organ disease'),
(6, 'immune disease'),
(7, 'venerological disease'),
(8, 'infectous disease'),
(9, 'dermal disease'),
(10, 'mental illnesses');


INSERT INTO Country (cname, population) VALUES
("Austria",	9000000),
("China",	1439000000),
("France",	65000000),
("Hungary",	9600000),
("Kazakhstan",	18000000),
("Mongolia",	3278000),
("North Korea",	25000000),
("Russia",	145000000),
("South Korea",	51000000),
("Turkey",	85000000),
("UK",	67000000),
("USA",	331000000);

INSERT INTO Disease (disease_code, pathogen, description, id) VALUES
('cancer', 'cell function', 'lethal illness', 1),
('fungus', 'bacterial', 'curable disease', 2),
('angina', 'bacterial', 'curable disease', 3),
('covid', 'virus', 'curable disease', 4),
('brain eating parasite', 'parasite', 'lethat 100%', 5),
('rabies', 'virus', 'lethal', 6),
('erectile disfunction', 'physical', 'curable', 7),
('HIV', 'virus', 'almost lethal', 8),
('AIDS', 'virus', 'lethal', 9),
('tetanus', 'virus + bacteria', 'can get from rusty nails', 10);

INSERT INTO Discover (cname, disease_code, first_enc_date) VALUES
('Kazakhstan', 'cancer', '2006-02-10'),
('USA', 'covid', '2006-02-16'),
('China', 'brain eating parasite', '2006-02-17'),
('France', 'rabies', '2006-02-20'),
('Mongolia', 'erectile disfunction', '2006-02-22'),
('South Korea', 'HIV', '2006-02-23'),
('North Korea', 'AIDS', '2006-02-24'),
('Turkey', 'tetanus', '2006-02-27'),
("Austria",	"angina",	"1800-02-15");


INSERT INTO Users (email, name, surname, salary, phone, cname) VALUES
("bahidam920@adroh.com",	"Demar",	"Derozan",	64356,	"4324213",	"China"),
("facikif348@3mkz.com",	"Kawhi",	"Leonard",	63456,	"4132234",	"USA"),
("fajoxe6837@abudat.com",	"Alla",	"Pugacheva",	4356,	"24314323",	"Russia"),
("givomob249@3mkz.com",	"Walter",	"White",	3465,	"423142134",	"France"),
("hipare5882@adroh.com",	"Clementine",	"Johnson",	546345,	"34252335443",	"UK"),
("jobin47996@3mkz.com",	"Cecil",	"Adams",	4484,	"94389023",	"Kazakhstan"),
("livato7934@3mkz.com",	"Jake",	"Gyllenhaal",	63456,	"423421111",	"South Korea"),
("repey86866@3mkz.com",	"Stephen",	"Curry",	63456,	"421421342",	"Turkey"),
("sisoja4145@adroh.com",	"Frank",	"Ocean",	63456,	"4234234",	"North Korea"),
("tocamo3972@24rumen.com",	"Gustavo",	"Fring",	63456,	"42342",	"Mongolia"),
("user.surname1@mail.kz",	"Skyler",	"White",	500,	"88005553535",	"USA"),
("user.surname2@mail.kz",	"Walter Jr.",	"White",	500,	"88005553536",	"USA");

INSERT INTO PublicServant (email, department) VALUES
('jobin47996@3mkz.com', 'D1'),
('hipare5882@adroh.com', 'D2'),
('fajoxe6837@abudat.com', 'D3'),
('facikif348@3mkz.com', 'D4'),
('bahidam920@adroh.com', 'D5'),
('givomob249@3mkz.com', 'D6'),
('tocamo3972@24rumen.com', 'D7'),
('livato7934@3mkz.com', 'D8'),
('sisoja4145@adroh.com', 'D9'),
('repey86866@3mkz.com', 'D10'),
("user.surname1@mail.kz"	"D11"),
("user.surname2@mail.kz"	"D11");

INSERT INTO Doctor (email, degree) VALUES
('jobin47996@3mkz.com', 'DoM'),
('hipare5882@adroh.com', 'DoM'),
('fajoxe6837@abudat.com', 'DoOM'),
('facikif348@3mkz.com', 'DoDM'),
('bahidam920@adroh.com', 'DoM'),
('givomob249@3mkz.com', 'DoM'),
('tocamo3972@24rumen.com', 'DoM'),
('livato7934@3mkz.com', 'BSN'),
('sisoja4145@adroh.com', 'MD'),
('repey86866@3mkz.com', 'DoM');


INSERT INTO Specialize (id, email) VALUES
(1, 'jobin47996@3mkz.com'),
(2, 'hipare5882@adroh.com'),
(3, 'fajoxe6837@abudat.com'),
(4, 'facikif348@3mkz.com'),
(5, 'bahidam920@adroh.com'),
(6, 'givomob249@3mkz.com'),
(7, 'tocamo3972@24rumen.com'),
(8, 'livato7934@3mkz.com'),
(9, 'sisoja4145@adroh.com'),
(10, 'repey86866@3mkz.com');


INSERT INTO Record (email, cname, disease_code, total_deaths, total_patients) VALUES
('jobin47996@3mkz.com', 'Kazakhstan', 'cancer', 132123, 42343),
('hipare5882@adroh.com', 'UK', 'fungus', 3123, 234423),
('fajoxe6837@abudat.com', 'Russia', 'angina', 13232,  23423),
('facikif348@3mkz.com', 'USA', 'covid', 1321,  4234),
('bahidam920@adroh.com', 'China', 'brain eating parasite', 12,  432432),
('givomob249@3mkz.com', 'France', 'rabies', 31231,  442323),
('tocamo3972@24rumen.com', 'Mongolia', 'erectile disfunction', 3123,  42342),
('livato7934@3mkz.com', 'South Korea', 'HIV', 3213211, 42342),
('sisoja4145@adroh.com', 'North Korea', 'AIDS', 132132,  24432),
('repey86866@3mkz.com', 'Turkey', 'tetanus', 312,  42342),
("user.surname1@mail.kz",	"China",	"covid",	2222,	3333),
("user.surname1@mail.kz",	"France",	"covid",	22223,	4444),
("user.surname1@mail.kz",	"Mongolia",	"covid",	2223,	223),
("user.surname1@mail.kz",	"USA",	"covid",	1221,	222),
("user.surname2@mail.kz",	"China",	"covid",	232,	32),
("user.surname2@mail.kz",	"Mongolia",	"covid",	3444,	33),
("user.surname2@mail.kz",	"Russia",	"covid",	2332,	233),
("user.surname2@mail.kz",	"USA",	"covid",	48484,	4343);