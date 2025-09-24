# character.py

class Character:
    """
    RPG 게임 캐릭터를 나타내는 클래스입니다.
    """
    def __init__(self, name, level=1, xp=0, quests_completed=0):
        self.name = name
        self.level = level
        self.xp = xp
        self.quests_completed = quests_completed

    def gain_xp(self, amount):
        """경험치를 획득하고 레벨업을 확인합니다."""
        self.xp += amount
        print(f"🎉 {self.name}가 경험치 {amount}를 획득했습니다!")
        self.check_level_up()

    def complete_quest(self):
        """퀘스트를 완료합니다."""
        self.quests_completed += 1
        print(f"✅ {self.name}가 퀘스트를 완료했습니다! (총 완료 퀘스트: {self.quests_completed})")
        self.gain_xp(50)  # 퀘스트 완료 시 경험치 보상

    def check_level_up(self):
        """레벨업 조건을 확인하고 레벨을 올립니다."""
        while self.xp >= self.level * 100:
            self.xp -= self.level * 100
            self.level += 1
            print(f"⭐ 축하합니다! {self.name}의 레벨이 {self.level}로 올랐습니다!")
    
    def display_status(self):
        """현재 캐릭터의 상태를 출력합니다."""
        print("\n--- 캐릭터 상태 ---")
        print(f"이름: {self.name}")
        print(f"레벨: {self.level}")
        print(f"경험치: {self.xp}/{self.level * 100}")
        print(f"완료한 퀘스트: {self.quests_completed}")
        print("-------------------")


def check_homework_status(character):
    """
    숙제 완료 조건을 확인합니다.
    (예: 레벨 10 이상, 퀘스트 3개 완료)
    """
    required_level = 10
    required_quests = 3

    print("\n--- 숙제 체크 ---")
    if character.level >= required_level and character.quests_completed >= required_quests:
        print("🚀 모든 숙제를 완료했습니다! 게임을 즐기세요!")
        return True
    else:
        print("아직 숙제가 남았네요. 더 열심히 해야 해요!")
        print(f"- 목표 레벨: {required_level} (현재 레벨: {character.level})")
        print(f"- 목표 퀘스트: {required_quests}개 (현재 완료: {character.quests_completed}개)")
        return False

# 메인 실행 코드
if __name__ == "__main__":
    player_name = input("플레이어의 이름을 입력하세요: ")
    player = Character(player_name)
    player.display_status()

    while True:
        action = input("\n무엇을 하시겠습니까? (1: 퀘스트 완료, 2: 경험치 획득, 3: 상태 보기, 4: 숙제 체크, q: 종료) ")

        if action == '1':
            player.complete_quest()
        elif action == '2':
            try:
                xp_amount = int(input("획득할 경험치 양을 입력하세요: "))
                player.gain_xp(xp_amount)
            except ValueError:
                print("⚠️ 올바른 숫자를 입력해주세요.")
        elif action == '3':
            player.display_status()
        elif action == '4':
            if check_homework_status(player):
                break
        elif action == 'q':
            print("게임을 종료합니다.")
            break
        else:
            print("❗ 올바른 명령어를 입력해주세요.")