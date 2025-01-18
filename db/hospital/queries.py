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
