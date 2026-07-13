from typing import Protocol, Sequence
import allure


class HasId(Protocol):
    id: int

@allure.step("checl presence of user by id")
def check_presence_by_id(target_objects: Sequence[HasId], target_id, present: bool = True):
    target_list = target_objects
    target_ids = [target.id for target in target_list]

    if present:
        assert target_id in target_ids, f"ID {target_id} должен быть, но не найден"
    else:
        assert target_id not in target_ids, f"ID {target_id} не должен быть, но найден"
