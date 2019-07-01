from Signal import Signal

f = Signal(low_bound=0, high_bound=10, formula="{x0}**2")
result = f.get_value_at(5)
