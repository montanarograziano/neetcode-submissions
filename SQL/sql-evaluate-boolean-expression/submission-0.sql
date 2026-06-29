select a.left_operand, a.operator, a.right_operand,
    case when
        a.operator = '<' then c.value < d.value when
        a.operator = '>' then c.value > d.value else
        c.value = d.value end as value
from expressions a join variables c on a.left_operand = c.name
    join variables d on a.right_operand = d.name