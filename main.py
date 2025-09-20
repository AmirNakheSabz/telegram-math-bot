from telethon import TelegramClient, events
api_id = 000000
api_hash = ""
bot_token = ""
client = TelegramClient("session",api_id=api_id, api_hash=api_hash).start(bot_token=bot_token)


from sympy import symbols, Eq, solve
from sympy.parsing.sympy_parser import parse_expr
import re

def solve_eq(eq):
    left_str, right_str = [s.strip() for s in eq.split("=", 1)]
    vars_found = sorted(set(re.findall(r"[a-zA-Z]\w*", eq)))
    if not vars_found:
        vars_symbols = []
    else:
        sym_text = " ".join(vars_found)
        vs = symbols(sym_text)
        vars_symbols = vs if isinstance(vs, (list, tuple)) else [vs]
    local_dict = dict(zip(vars_found, vars_symbols))
    left_expr = parse_expr(left_str, local_dict=local_dict)
    right_expr = parse_expr(right_str, local_dict=local_dict)
    eq = Eq(left_expr, right_expr)
    if not vars_symbols:
        return eq, [] if not eq else [{"result": True}]
    solutions = solve(eq, vars_symbols, dict=True)
    return eq, solutions[0]

@client.on(events.NewMessage(pattern="/slove"))
async def give_res(event):
    text = event.text
    eqs = text.strip("/slove")
    equation, solution = solve_eq(eqs)
    await event.reply(f"""the given equation is {equation}
    and its solution is: {solution}
""")

@client.on(events.NewMessage(pattern="/compare"))
async def give_ress(event):
    text = event.text
    nums = re.findall(r'-?\d+', text)
    x, y = map(int, nums[:2])
    if x > y:
        await event.reply(f"the number {x} is greater than the number {y}")
    elif x < y:
        await event.reply(f"the number {y} is greater than the number {x}")
    elif x == y:
        await event.reply(f"the number {x} is equal to the number {y}")
    else:
        return
print("bot is running...")
client.run_until_disconnected()
