-- 코드를 작성해주세요
select item_id, item_name, rarity
from item_info 
where item_id not in (
    select distinct parent_item_id
    from item_tree
    -- PARENT_ITEM_ID가 NULL인 ROOT 아이템 제외
    where parent_item_id is not null)
order by item_id desc