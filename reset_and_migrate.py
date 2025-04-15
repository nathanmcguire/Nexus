import os
import shutil
import subprocess

# Paths
sqlite_db_path = "sqlite.db"
alembic_versions_path = "alembic/versions"

# Step 1: Delete the SQLite database file
if os.path.exists(sqlite_db_path):
    os.remove(sqlite_db_path)
    print(f"Deleted database file: {sqlite_db_path}")
else:
    print(f"Database file not found: {sqlite_db_path}")

# Step 2: Delete all migration files in alembic/versions
if os.path.exists(alembic_versions_path):
    for filename in os.listdir(alembic_versions_path):
        file_path = os.path.join(alembic_versions_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print(f"Cleared migration files in: {alembic_versions_path}")
else:
    print(f"Alembic versions directory not found: {alembic_versions_path}")

# Step 3: Generate a new migration
try:
    subprocess.run(["alembic", "revision", "--autogenerate", "-m", "initial_migration"], check=True)
    print("Generated new migration.")
except subprocess.CalledProcessError as e:
    print(f"Error generating migration: {e}")

# Step 4: Apply the migration
try:
    subprocess.run(["alembic", "upgrade", "head"], check=True)
    print("Applied migration.")
except subprocess.CalledProcessError as e:
    print(f"Error applying migration: {e}")

# Step 5: Display the generated migration script
migration_files = os.listdir(alembic_versions_path)
if migration_files:
    latest_migration = max(migration_files, key=lambda f: os.path.getctime(os.path.join(alembic_versions_path, f)))
    latest_migration_path = os.path.join(alembic_versions_path, latest_migration)
    print(f"\nGenerated Migration Script ({latest_migration}):\n")
    with open(latest_migration_path, 'r') as file:
        print(file.read())
else:
    print("No migration files found to display.")