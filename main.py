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
def gcollatz(n:int) -> str:
    start_n = n
    ns = []
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
            ns.append(n)
        else:
            n = int(3 * n + 1)
            ns.append(n)
    ststr = f"your starting number is {start_n}"
    result_str = "\n".join(f"the new number is {n}" for n in ns)
    return ststr + "\n" + result_str

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
@client.on(events.NewMessage(pattern="/collatz"))
async def return_collatz(event):
    text = event.text
    parts = text.split(maxsplit=1)
    if len(parts) != 2 or not parts[1].isdigit():
        await event.reply("Usage: `/collatz <number>`")
        return
    n = int(parts[1])
    result = gcollatz(n=n)
    await event.reply(result)
print("bot is now running...")
client.run_until_disconnected()
