from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['env.yaml', '.secrets.yaml'],
    environments=True,
    merge_enabled=True,
)
