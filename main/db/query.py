from db.model import Korea_1st, Korea_2nd, Korea_3rd, Korea_4th
from sqlalchemy import select, func

dong = (select(Korea_3rd.emd_cd, func.substring(Korea_3rd.emd_cd, 1, 5).label('up_cd'), Korea_3rd.emd_kor_nm)).alias('dong')
gu = (select(Korea_2nd.sig_cd, func.substring(Korea_2nd.sig_cd, 1, 2).label('up_cd'), Korea_2nd.sig_kor_nm)).alias('gu')
si = (select(Korea_1st.ctprvn_cd, Korea_1st.ctp_kor_nm)).alias('si')

def si_gu_dong(x, y):
    dong = (
        select(Korea_3rd.emd_cd, func.substring(Korea_3rd.emd_cd, 1, 5).label('up_cd'), Korea_3rd.emd_kor_nm)
        .where(func.geometry_within(func.ST_SetSRID(func.ST_GeomFromText(f'POINT({x} {y})'), 4326), Korea_3rd.geom))
        .limit(1)
    ).alias('dong')
    
    result = (
        select(si.c.ctp_kor_nm, gu.c.sig_kor_nm, dong.c.emd_kor_nm)
        .select_from(dong)
        .join(gu, dong.c.up_cd == gu.c.sig_cd)
        .join(si, gu.c.up_cd == si.c.ctprvn_cd)
    )
    
    return result


def si_gu_dong_ri(x, y):
    ri = (
         select(Korea_4th.li_cd, func.substring(Korea_4th.li_cd, 1, 8).label('up_cd'), Korea_4th.li_kor_nm)
        .where(func.geometry_within(func.ST_SetSRID(func.ST_GeomFromText(f'POINT({x} {y})'), 4326), Korea_4th.geom))
        .limit(1)
    ).alias('ri')

    result = (
        select(si.c.ctp_kor_nm, gu.c.sig_kor_nm, dong.c.emd_kor_nm, ri.c.li_kor_nm)
        .select_from(ri)
        .join(dong, ri.c.up_cd == dong.c.emd_cd)
        .join(gu, dong.c.up_cd == gu.c.sig_cd)
        .join(si, gu.c.up_cd == si.c.ctprvn_cd)
    )
    

    return result