const Player = require('../models/player.js');
const assert = require('assert');

describe('Player', function () {
  let player;
  beforeEach(function () {
    player = new Player();
  })
  it('should allow move', () => {
    player.move(3)
    const actual = player.position;
    assert.strictEqual(actual, 3);
  })
  it('should allow move/wrap', () => {
    player.move(30)
    const actual = player.position;
    assert.strictEqual(actual, 0);
  })
  it('should get correct category', () => {
    const actual = player.getCategoryObject().category;
    assert.strictEqual(actual, 'haskell');
  })
  it('should get category after a move', () => {
    player.move(3)
    const actual = player.getCategoryObject().category;
    assert.strictEqual(actual, 'nova-things');
  })
  it('should get pie piece', () => {
    player.getPie('nova-things')
    const expected = {'nova-things': true};
    const actual = player.pie;
    assert.deepStrictEqual(actual, expected);
  })
  it('should know when player has not won', () => {
    assert.strictEqual(player.checkWin(), false);
  })
  it('should know when player has won', () => {
    player.getPie('haskell');
    player.getPie('nova-things');
    player.getPie('python');
    player.getPie('web');
    assert.strictEqual(player.checkWin(), true);
  })
});
