from sqlalchemy import Column, Integer, String, Text, DateTime
from db.database import Base

class Korea_1st(Base):
    __tablename__ = 'korea_1st'

    ctprvn_cd = Column(Integer, primary_key=True)
    ctp_kor_nm = Column(String, nullable=False)
    geom = Column(Text, nullable=False)

class Korea_2nd(Base):
    __tablename__ = 'korea_2nd'

    sig_cd = Column(Integer, primary_key=True)
    sig_kor_nm = Column(String, nullable=False)
    geom = Column(Text, nullable=False)

class Korea_3rd(Base):
    __tablename__ = 'korea_3rd'

    emd_cd = Column(Integer, primary_key=True)
    emd_kor_nm = Column(Integer, nullable=False)
    geom = Column(Text, nullable=False)

class Korea_4th(Base):
    __tablename__ = 'korea_4th'

    li_cd = Column(Integer, primary_key=True)
    li_kor_nm = Column(Integer, nullable=False)
    geom = Column(Text, nullable=False)


