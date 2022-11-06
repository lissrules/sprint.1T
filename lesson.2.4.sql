--Попробуйте вывести не просто самую высокую зарплату во всей команде, а вывести именно фамилию сотрудника с самой высокой зарплатой.
select sfio from tblsotr where ilevelbonus = (SELECT Max(ilevelbonus) FROM tblsotr)
-- Попробуйте вывести фамилии сотрудников в алфавитном порядке
select sfio from tblsotr order by sfio asc
--Рассчитайте средний стаж для каждого уровня сотрудников
select s2.status, AVG(((EXTRACT(epoch FROM age(now(), dtNaznach)) / 86400)/365))::integer 
from tblsotr s1, tblgrade s2
where s1.grade_id = s2.grade_id
group by s2.status
-- Выведите фамилию сотрудника и название отдела, в котором он работает
select s1.sfio, s2.namedepart
from tblsotr s1, tbldepart s2
where s1.department_id = s2.department_id
order by s2.namedepart desc
--Выведите название отдела и фамилию сотрудника с самой высокой зарплатой в данном отделе и саму зарплату также.
select s1.sfio, s2.namedepart, ilevelbonus
from tblsotr s1, tbldepart s2
where s1.department_id = s2.department_id
and ilevelbonus = (SELECT Max(ilevelbonus) FROM tblsotr)
order by s2.namedepart desc
--Выведите название отдела, сотрудники которого получат наибольшую премию по итогам года. Как рассчитать премию можно узнать в последнем задании предыдущей домашней работы
SELECT s3.namedepart, sum(s1.koef) as CommonBonus
FROM tblsotr s2, tbldepart s3,
(SELECT person_id,
	SUM(case 
		when ball = 'A' then 0.2
		when ball = 'B' then 0.1
		when ball = 'C' then 1
		when ball = 'D' then -0.1
		when ball = 'E' then -0.2
	end) koef
FROM tblbonuslist
group by person_id) as s1
where s2.person_id = s1.person_id
and s3.department_id = s2.department_id
group by s3.namedepart
order by CommonBonus desc
limit 1
--Проиндексируйте зарплаты сотрудников с учетом коэффициента премии. Для сотрудников с коэффициентом премии больше 1.2 – размер индексации составит 20%, для сотрудников с коэффициентом премии от 1 до 1.2 размер индексации составит 10%. Для всех остальных сотрудников индексация не предусмотрена.
SELECT s2.sfio, s3.namedepart, s1.koef, s2.ilevelbonus as oldBonus, 
(case
 when s1.koef >= 1.2 then s2.ilevelbonus*1.2
 when s1.koef >= 1 and s1.koef < 1.2  then s2.ilevelbonus*1.1
 else s2.ilevelbonus
 end) as newBonus
FROM tblsotr s2, tbldepart s3,
(SELECT person_id,
	SUM(case 
		when ball = 'A' then 0.2
		when ball = 'B' then 0.1
		when ball = 'C' then 1
		when ball = 'D' then -0.1
		when ball = 'E' then -0.2
	end) koef
FROM tblbonuslist
group by person_id) as s1
where s2.person_id = s1.person_id
and s3.department_id = s2.department_id
