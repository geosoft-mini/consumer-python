import pandas as pd
from db.database import SessionLocal
from models.model import Korea_1st, Korea_2nd, Korea_3rd, Korea_4th
from sqlalchemy import select, func, and_
from sqlalchemy.orm import aliased
from sqlalchemy.sql import literal_column
from datetime import datetime

db = SessionLocal()
data = pd.read_csv('list.csv', encoding='utf-8')

x_list = data.iloc[:,4]
y_list = data.iloc[:,5]

x_list = x_list[:100]
y_list = y_list[:100]


subquery_b = (
    select(
        Korea_3rd.emd_cd,
        func.substring(Korea_3rd.emd_cd, 1, 5).label('up_cd'),
        Korea_3rd.emd_kor_nm
    )
).alias('B')

subquery_c = (
    select(
        Korea_2nd.sig_cd,
        func.substring(Korea_2nd.sig_cd, 1, 2).label('up_cd'),
        Korea_2nd.sig_kor_nm
    )
).alias('C')

subquery_d = (
    select(
        Korea_1st.ctprvn_cd,
        Korea_1st.ctp_kor_nm
    )
).alias('D')

def __si_gu_dong(x, y):
    subquery_b = (
        select(
            Korea_3rd.emd_cd,
            func.substring(Korea_3rd.emd_cd, 1, 5).label('up_cd'),
            Korea_3rd.emd_kor_nm
        )
        .where(func.ST_Within(func.ST_SetSRID(func.ST_GeomFromText(f'POINT({x} {y})'), 4326), Korea_3rd.geom))
        .limit(1)
    ).alias('B')

    return (
        select(
            subquery_d.c.ctp_kor_nm,
            subquery_c.c.sig_kor_nm,
            subquery_b.c.emd_kor_nm
        )
        .select_from(subquery_b)
        .join(subquery_c, subquery_b.c.up_cd == subquery_c.c.sig_cd)
        .join(subquery_d, subquery_c.c.up_cd == subquery_d.c.ctprvn_cd)
    )



def __si_gu_dong_li(x, y):
    subquery_a = (
         select(
            Korea_4th.li_cd,
            func.substring(Korea_4th.li_cd, 1, 8).label('up_cd'),
            Korea_4th.li_kor_nm
        )
        .where(func.ST_Within(func.ST_SetSRID(func.ST_GeomFromText(f'POINT({x} {y})'), 4326), Korea_4th.geom))
        .limit(1)
    ).alias('A')

    return (
        select(
            subquery_d.c.ctp_kor_nm,
            subquery_c.c.sig_kor_nm,
            subquery_b.c.emd_kor_nm,
            subquery_a.c.li_kor_nm,
        )
        .select_from(subquery_a)
        .join(subquery_b, subquery_a.c.up_cd == subquery_b.c.emd_cd)
        .join(subquery_c, subquery_b.c.up_cd == subquery_c.c.sig_cd)
        .join(subquery_d, subquery_c.c.up_cd == subquery_d.c.ctprvn_cd)
    )


now = datetime.now()

for pair in zip(x_list, y_list):
    result = db.execute(__si_gu_dong_li(pair[0], pair[1])).fetchone()

    if not result:
        result = db.execute(__si_gu_dong(pair[0], pair[1])).fetchone()

end = datetime.now()
print(end - now)



