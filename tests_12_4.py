import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:

            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    # is_frozen = False

    # @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            Runner1 = Runner('Денис', speed=-5)
            for _ in range(10):
                Runner1.walk()
            self.assertEqual(Runner1.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner')
            raise e

    # @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            Runner2 = Runner(1234)
            for _ in range(10):
                Runner2.run()
            self.assertEqual(Runner2.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner')
            raise e

    # @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        Runner3 = Runner('Дима')
        Runner4 = Runner('Вика')
        for _ in range(10):
            Runner3.run()
            Runner4.walk()
        self.assertNotEqual(Runner3.distance, Runner4.distance)


if __name__ == '__main__':
    unittest.main()
else:
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log',
                        encoding='utf-8', format='%(levelname)s | %(message)s')

