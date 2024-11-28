{% test less_than_or_equal(model, column_name, compare_model, compare_column) %}

with compared_values as (
    select
        a.{{ column_name }} as value,
        b.{{ compare_column }} as compare_value
    from {{ model }} a
    cross join {{ compare_model }} b
)

select *
from compared_values
where value > compare_value

{% endtest %}
