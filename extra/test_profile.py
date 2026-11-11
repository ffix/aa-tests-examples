def format_profile(name: str, city: str) -> str:
    return f"{name.strip()} — {city.strip()}"

def test_profile_trims_input(faker):
    name = faker.name()
    city = faker.city()
    result = format_profile(f"  {name}  ", f" {city} ")
    assert result == f"{name} — {city}"
