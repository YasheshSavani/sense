##Objective

Everyone has played badminton at least once in their lifetime. To play, we need to learn different shots and for that
we take help from coaches, tournament videos, books and last we do practice everyday.

But, after lots of practice, if you want to know that how perfect are your shots or what shot that international
player played in the video, how will you do that?

So, at that time, this application <b><code>Badminton Shot Recognition</code></b> can be used, which will provide realtime feedback by
recognizing your badminton shots.


##Dataset Breakdown

There are <code>17</code> different classes (badminton shots + background activity + no racket actions) on which this model is
trained using transfer learning on top of the weights provided by <code>sense</code> repository.

Number of total videos: 278<br/>
Duration of videos: 4 to 5 seconds<br/>
Dataset distribution: (approx) 70% train, 30% valid (Each class)<br/>

<table>
    <tr>
        <th>Classes</th>
        <th>Train set</th>
        <th>Validation set</th>
    </tr>
    <tr>
        <td>with_racket</td>
        <td>11</td>
        <td>3</td>
    </tr>
    <tr>
        <td>without_racket</td>
        <td>14</td>
        <td>6</td>
    </tr>
    <tr>
        <td>no_person_visible</td>
        <td>12</td>
        <td>5</td>
    </tr>
    <tr>
        <td>getting_into_position</td>
        <td>11</td>
        <td>5</td>
    </tr>
    <tr>
        <td>forward_forehand_shot</td>
        <td>11</td>
        <td>5</td>
    </tr>    
    <tr>
        <td>forward_backhand_shot</td>
        <td>11</td>
        <td>5</td>
    </tr>    
    <tr>
        <td>forehand_underhead_shot</td>
        <td>11</td>
        <td>5</td>
    </tr>    
    <tr>
        <td>backhand_underhead_shot</td>
        <td>11</td>
        <td>5</td>
    </tr>    
    <tr>
        <td>forehand_overhead_shot</td>
        <td>11</td>
        <td>5</td>
    </tr>    
    <tr>
        <td>backhand_overhead_shot</td>
        <td>11</td>
        <td>5</td>
    </tr>    
    <tr>
        <td>forehand_side_shot</td>
        <td>12</td>
        <td>3</td>
    </tr>    
    <tr>
        <td>backhand_side_shot</td>
        <td>11</td>
        <td>5</td>
    </tr>    
    <tr>
        <td>forehand_backcourt_shot</td>
        <td>11</td>
        <td>5</td>
    </tr>    
    <tr>
        <td>backhand_backcourt_shot</td>
        <td>11</td>
        <td>5</td>
    </tr>
    <tr>
        <td>forehand_serve</td>
        <td>13</td>
        <td>5</td>
    </tr>
    <tr>
        <td>backhand_serve</td>
        <td>12</td>
        <td>5</td>
    </tr>
    <tr>
        <td>doing_nothing</td>
        <td>12</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Total</td>
        <td>196</td>
        <td>82</td>
    </tr>
</table>


## Examples of classes
<img src="../assets/badminton_shots/With_racket.gif" alt="With racket">
| With Racket | Without racket | Forward Forehand shot | Forward Backhand shot |
| --- | --- | --- | --- |
| ![With Racket](../assets/badminton_shots/With_racket.gif) | ![With Racket](../assets/badminton_shots/Without_racket.gif) | ![With Racket](../assets/badminton_shots/Forward_forehand_shot.gif) | ![With Racket](../assets/badminton_shots/Forward_backhand_shot.gif) |

| Forehand Overhead shot | Backhand Overhead shot | Forehand Serve | Backhand Serve |  |
| --- | --- | --- | --- | --- |
| ![With Racket](../assets/badminton_shots/With_racket.gif) | ![With Racket](../assets/badminton_shots/With_racket.gif) | ![With Racket](../assets/badminton_shots/With_racket.gif) | ![With Racket](../assets/badminton_shots/With_racket.gif) | ![With Racket](../assets/badminton_shots/With_racket.gif) |

| With Racket | Without racket | Without racket | Without racket | With Racket |
| --- | --- | --- | --- | --- |
| }![With Racket](../assets/badminton_shots/With_racket.gif) | ![With Racket](../assets/badminton_shots/With_racket.gif) | ![With Racket](../assets/badminton_shots/With_racket.gif) | ![With Racket](../assets/badminton_shots/With_racket.gif) | ![With Racket](../assets/badminton_shots/With_racket.gif) |


