ins_departments = (
    'insert into departments '
    '  (name) '
    'values '
    '  (%s) '
)
ins_sponsors = (
    'insert into sponsors '
    '  (name) '
    'values '
    '  (%s) '
)
ins_specializations = (
    'insert into specializations '
    '  (name) '
    'values '
    '  (%s) '
)
ins_wards = (
    'insert into wards '
    '  (dep_id, name) '
    'values '
    '  (%s, %s) '
)
ins_donations = (
    'insert into donations '
    '  (sponsor_id, dep_id, date, amount) '
    'values '
    '  (%s, %s, %s, %s) '
)
ins_doctors = (
    'insert into doctors '
    '  (dep_id, last_name, first_name, patr_name, salary, premium) '
    'values '
    '  (%s, %s, %s, %s, %s, %s) '
)
ins_doctors_specs = (
    'insert into doctors_specs '
    '  (doctor_id, spec_id) '
    'values '
    '  (%s, %s) '
)
ins_vacations = (
    'insert into vacations '
    '  (doctor_id, start_date, end_date) '
    'values '
    '  (%s, %s, %s) '
)


sel_donations_by_year = '''
    select
      extract(year from "date") as year,
      sum(amount)
    from
      donations
    group by
      year
    order by
      year
'''

sel_donations_by_year_and_dep = '''
    select
      extract(year from "date") as year,
      dep_id,
      sum(amount)
    from
      donations
    group by
      year, 
      dep_id
    order by
      year,
      dep_id
'''

sel_count_week_vacations = '''
    select
      case when end_date - start_date <= 7 then 'неделя'
           else 'больше недели'
      end as week_or_more,
      count(*)
    from 
      vacations
    group by
      week_or_more
'''

sel_wards_departments = '''
    select 
      wards.name,
      departments.name
    from
      wards
    join
      departments on dep_id = departments.id
'''

sel_groupconcat_wards_departments = '''
      select d.name as "отделение",
             string_agg(w.name, ', ') as "палаты"
        from wards as w
        join departments as d
          on dep_id = d.id
    group by d.name
'''

sel_large_donations = '''
      select d.name as "отделение",
             s.name as "спонсор",
             date as "дата",
             amount as "сумма"
        from departments as d
        join donations
          on d.id = dep_id and d.id between 2 and 5
        join sponsors as s
          on sponsor_id = s.id and amount > 500000
    order by "отделение", "сумма"
'''

sel_all_doctors_specs = '''
       select concat_ws(' ', last_name, first_name, patr_name) as "ФИО",
              string_agg(s.name, ', ') as "Специальность"
         from doctors as d
    left join doctors_specs on d.id = doctor_id
    left join specializations as s on spec_id = s.id
     group by "ФИО"
     order by "ФИО"
'''

sel_doctors_cnt_for_spec = '''
        select s.name as "Специальность",
               count(doctor_id) as "Кол-во врачей"
          from doctors_specs
    right join specializations as s on spec_id = s.id
      group by s.name
      order by "Кол-во врачей" desc;
'''

sel_vac_cnt_for_last_two_years = '''
    select 
      name,
      count(v.id)
    from 
      vacations as v
    join 
      doctors as d on doctor_id = d.id 
                   and extract(year from start_date) >= extract(year from current_date) - 2
    join 
      departments as dep on dep_id = dep.id
    group by 
      name
    order by
      name;
'''

sel_avg_vacations_cnt = '''
    select 
      round(avg(subq.cnt), 1) as "average vacations"
    from (
      select
        doctor_id,
        count(*) as cnt
      from 
        vacations
      group by
        doctor_id
    ) as subq
'''

sel_max_income_by_spec = '''
    select
      concat_ws(' ', last_name, first_name, patr_name) as "ФИО",
      ext_d.salary + ext_d.premium as "Доход"
    from 
      doctors as ext_d
    join (
      select 
        max(salary + premium) as "Доход",
        coalesce(s.name, 'Младший персонал') as "Специальность"
      from
        doctors as d
      left join 
        doctors_specs on d.id = doctor_id
      left join 
        specializations as s on spec_id = s.id
      group by 
        "Специальность"
    ) as subq on subq."Доход" = ext_d.salary + ext_d.premium
'''

sel_doctors_salary_lt_avg = '''
    select
      concat_ws(' ', last_name, first_name, patr_name) as full_name,
      salary
    from
      doctors
    where salary < (select avg(salary) from doctors)
'''

sel_countries_area_by_region_with_total = '''
    select 
      concat(Continent, ' — ', Region) as cont_reg,
      sum(SurfaceArea) as area
    from 
      country
    group by 
      cont_reg
    union
    select 
      "Total",
      sum(SurfaceArea)
    from 
      country
    order by
      cont_reg,
      area
'''

sel_min_max_in_one_col = '''
    select 'минимальное городское население' as q, min(Population) from city
    union
    select 'максимальное городское население' as q, max(Population) from city
'''

sel_mln_cities_gt_5 = '''
    select
      country.name
    from
      city
    join 
      country on countrycode = code 
              and city.population > 1000000
    group by
      country.name
    having
      count(*) > 5
    order by
      country.name
'''

sel_spanish_longlive = '''
      select c.name
        from country as c
        join countrylanguage as cl 
          on countrycode = code
         and lifeexpectancy > 70
         and isofficial = 'T'
    group by c.name
      having group_concat('', language) like '%Spanish%'
         and count(*) = 1
    order by c.name
'''

sel_dep_specs = '''
    select
      subq.dep_name,
      string_agg(subq.spec, ', ') as specs
    from (
      select distinct
        dep.name as dep_name,
        s.name as spec
      from
        departments as dep
      join
        doctors as d on dep.id = dep_id
      join
        doctors_specs on d.id = doctor_id
      join
        specializations as s on spec_id = s.id
      order by
        dep.name,
        s.name
    ) as subq
    group by
      subq.dep_name
'''

sel_sepcs = 'select name from specializations'

