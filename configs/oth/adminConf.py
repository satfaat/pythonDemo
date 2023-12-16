# AMIS-ADMIN
from fastapi_amis_admin import i18n
from fastapi_amis_admin.admin.settings import Settings
from fastapi_amis_admin.admin.site import AdminSite
from fastapi_amis_admin.admin import admin
from configs.dbConf.dbParams import sqlite_url


i18n.set_language(language='en_US')
amis_admin = AdminSite(settings=Settings(
    database_url=sqlite_url))
