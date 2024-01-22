import { ASSETS_URL } from '.'

const fileLoader = game => {
    game.load.crossOrigin = 'Anonymous'
    game.stage.backgroundColor = '#1E1E1E'
    game.load.image('asphalt', `${ASSETS_URL}/sprite/asphalt/asphalt.webp`)
    game.load.image('car', `${ASSETS_URL}/sprite/car/car.webp`)
}
export default fileLoader