SELECT
    e.left_operand,
    e.operator,
    e.right_operand,
    CASE e.operator
        WHEN '>' THEN (lv.value > rv.value)
        WHEN '<' THEN (lv.value < rv.value)
        WHEN '=' THEN (lv.value = rv.value)
    END AS value
FROM expressions e
JOIN variables lv ON lv.name = e.left_operand
JOIN variables rv ON rv.name = e.right_operand;