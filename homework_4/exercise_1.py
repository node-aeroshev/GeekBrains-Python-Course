from typing import Dict, Optional
from sys import argv


def cli() -> Optional[Dict[str, float]]:
    try:
        _, hours, pay_per_hour, prize = argv
        try:
            hours = float(hours)
            pay_per_hour = float(pay_per_hour)
            prize = float(prize)
            return {
                "hours": hours,
                "pay_per_hour": pay_per_hour,
                "prize": prize
            }
        except ValueError as err:
            return None
    except ValueError as err:
        return None


def calculate(data: Dict[str, float]) -> float:
    if data:
        return data.get("hours", 0.0) * data.get("pay_per_hour", 0.0) + data.get("prize", 0.0)
    else:
        return 0.0


if __name__ == '__main__':
    _data = cli()
    money = calculate(_data)
    print("Money bro = ", money)
