from sqlalchemy import create_engine, text
import os

db_connection_string = "mysql+pymysql://wfmzeg4jpdvujfgn2bf4:pscale_pw_pIpnGSbLXL9suN6biB1zFGvaAwyRyHkEiTyFoooD1e0@aws.connect.psdb.cloud/browndataguy?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       pool_pre_ping=True,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def loads_websites_from_db():
  # connecting the data with the engine/ useful is showing data on homepage
  with engine.connect() as conn:
    result = conn.execute(text("select * from websites"))
    web = []
    for row in result.all():
      web.append(row._asdict())
    return web



