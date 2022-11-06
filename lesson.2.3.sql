 --Уникальный номер сотрудника, его ФИО и стаж работы – для всех сотрудников компании
 SELECT "tblSotr"."PersonID",
    "tblSotr"."sFIO",
    ((EXTRACT(epoch FROM age(now(), "tblSotr"."dtNaznach")) / 86400)/365)::integer as Stage
   FROM "tblSotr";
   
 --Уникальный номер сотрудника, его ФИО и стаж работы – только первых 3-х сотрудников
  SELECT "tblSotr"."PersonID",
    "tblSotr"."sFIO",
    ((EXTRACT(epoch FROM age(now(), "tblSotr"."dtNaznach")) / 86400)/365)::integer as Stage
   FROM "tblSotr"
   fetch first 3 rows only;
   
  --Уникальный номер сотрудников - водителей
   SELECT "tblSotr"."PersonID"
   FROM "tblSotr"
   WHERE "tblSotr"."bAccAuto" = true;
   
   --Выведите номера сотрудников, которые хотя бы за 1 квартал получили оценку D или E
   SELECT distinct "tblBonusList"."PersonID"
   FROM "tblBonusList"
   WHERE "tblBonusList"."Ball" in ('D', 'E');
   
   --Выведите самую высокую зарплату в компании.
   SELECT Max("tblSotr"."iLevelBonus")
   FROM "tblSotr";
  	
	--Выведите название самого крупного отдела
	SELECT "tblDepart"."NameDepart"
	FROM "tblDepart"
	WHERE "tblDepart"."NumberOfPerson" = (SELECT MAX("tblDepart"."NumberOfPerson") FROM "tblDepart");
	
	--Выведите номера сотрудников от самых опытных до вновь прибывших
	 SELECT "tblSotr"."PersonID",
    ((EXTRACT(epoch FROM age(now(), "tblSotr"."dtNaznach")) / 86400)/365)::integer as Stage
   	FROM "tblSotr"
	order by Stage desc;
	
	-- Рассчитайте среднюю зарплату для каждого уровня сотрудников
	SELECT "tblGrade"."Status", AVG("tblSotr"."iLevelBonus")::integer
   	FROM "tblSotr","tblGrade"
	Where "tblGrade"."GradeID"="tblSotr"."GradeID"
	group by "tblGrade"."Status"
	order by "tblGrade"."Status";
   
   SELECT "tblSotr".*, s1.koef
   FROM "tblSotr",
   (SELECT "tblBonusList"."PersonID",
   		SUM(case 
   			when "tblBonusList"."Ball" = 'A' then 0.2
			when "tblBonusList"."Ball" = 'B' then 0.1
			when "tblBonusList"."Ball" = 'C' then 1
			when "tblBonusList"."Ball" = 'D' then -0.1
			when "tblBonusList"."Ball" = 'E' then -0.2
		end) koef
   FROM "tblBonusList"
   group by "tblBonusList"."PersonID") as s1
   where "tblSotr"."PersonID" = s1."PersonID"