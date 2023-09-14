{% macro limitrows(columnname) %}
where {{ columnname }} <= current_timestamp()
{% endmacro %}