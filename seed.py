import asyncio
from app.database import employee_details


async def seed_data():
    """Seed sample data into Employee_details collection."""
    # Check if data already exists to avoid duplicates
    existing = await employee_details.find_one({"EmpID": "E123"})
    if not existing:
        await employee_details.insert_one(
            {
                "EmpID": "E123",
                "name": "Vasu Gadde",
                "department": "Logistics",
            }
        )
    print("Sample data seeded.")


if __name__ == "__main__":
    asyncio.run(seed_data())