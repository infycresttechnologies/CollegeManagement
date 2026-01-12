import django.db.backends.mysql.base
from django.db.backends.mysql.features import DatabaseFeatures

# Bypass version check
django.db.backends.mysql.base.DatabaseWrapper.check_database_version_supported = lambda self: None

# Disable unsupported features for older MariaDB
DatabaseFeatures.can_return_columns_from_insert = False
